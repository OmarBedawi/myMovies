import os
from flask import Flask, flash, render_template, redirect, request, session, url_for  # noqa: disable=line-too-long
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask import json

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("get_films", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("index.html")


@app.route("/all_films")
def all_films():
    films = list(mongo.db.films.find().sort("title"))
    for film in films:
        try:
            film["created_by"] = mongo.db.users.find_one(
                {"_id": ObjectId(film["created_by"])}
            )["username"]
        except Exception:
            pass
    return render_template("all_films.html", films=films)


@app.route("/get_films")
def get_films():
    try:
        user_id = mongo.db.users.find_one({"username": session["user"]})["_id"]
        films = list(mongo.db.films.find({"created_by": user_id}).sort("title"))  # noqa: disable=line-too-long
        for film in films:
            try:
                film["created_by"] = mongo.db.users.find_one(
                    {"_id": ObjectId(film["created_by"])}
                )["username"]
            except Exception:
                pass
            try:
                film["comments"] = list(film["comments"])
            except KeyError:
                film["comments"] = []
        return render_template("my_films.html", films=films, username=session["user"])  # noqa: disable=line-too-long
    except KeyError:
        return redirect(url_for("login"))
    except Exception:
        raise


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    films = list(mongo.db.films.find({"$text": {"$search": query}}).sort("title"))  # noqa: disable=line-too-long
    for film in films:
        try:
            film["created_by"] = mongo.db.users.find_one(
                {"_id": ObjectId(film["created_by"])}
            )["username"]
        except Exception:
            pass
    return render_template("all_films.html", films=films)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("get_films", username=session["user"]))

    return render_template("register.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one({"username": session["user"]})["username"]  # noqa: disable=line-too-long

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_film", methods=["GET", "POST"])
def add_film():
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})
        film = {
            "title": request.form.get("title"),
            "genre": request.form.get("genre"),
            "year": request.form.get("year"),
            "wiki": request.form.get("wiki"),
            "created_by": ObjectId(user["_id"]),
            "cover": request.form.get("cover"),
        }
        mongo.db.films.insert_one(film)
        flash("Film Successfully Added")
        return redirect(url_for("get_films"))
    return render_template("add_film.html")


@app.route("/edit_film/<film_id>", methods=["GET", "POST"])
def edit_film(film_id):
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})
        submit = {
            "title": request.form.get("title"),
            "genre": request.form.get("genre"),
            "year": request.form.get("year"),
            "wiki": request.form.get("wiki"),
            "created_by": ObjectId(user["_id"]),
            "cover": request.form.get("cover"),
        }
        mongo.db.films.update({"_id": ObjectId(film_id)}, submit)
        flash("Film Successfully Updated")
        return redirect(url_for("get_films"))

    film = mongo.db.films.find_one({"_id": ObjectId(film_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_film.html", film=film, categories=categories)


@app.route("/delete_film/<film_id>")
def delete_film(film_id):
    mongo.db.films.remove({"_id": ObjectId(film_id)})
    flash("Film Successfully Deleted")
    return redirect(request.referrer)


@app.route("/comment", methods=["POST"])
def comment():
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})
        film_id = request.form.get('id')
        comment = request.form.get('comment')
        film = mongo.db.films.find_one({"_id": ObjectId(film_id)})
        try:
            current_comments = film['comments']
        except KeyError:
            current_comments = []
        new_comment = {'text': comment, 'author': user.get('username')}
        current_comments.append(new_comment)
        update = {
            "title": film.get("title"),
            "genre": film.get("genre"),
            "year": film.get("year"),
            "wiki": film.get("wiki"),
            "created_by": film.get("created_by"),
            "cover": film.get("cover"),
            "comments": current_comments
        }
        mongo.db.films.update({"_id": ObjectId(film_id)}, update)
        response = app.response_class(
            response=json.dumps(new_comment),
            status=200,
            mimetype='application/json'
        )
        return response


@app.route("/delete_film_comment/<film_id>/<comment>")
def delete_film_comment(film_id, comment):
    film = mongo.db.films.find_one({"_id": ObjectId(film_id)})
    current_comments = film['comments']
    updated_comments = list(filter(lambda x: x['text'] != comment, current_comments))  # noqa: disable=line-too-long
    update = {
        "title": film.get("title"),
        "genre": film.get("genre"),
        "year": film.get("year"),
        "wiki": film.get("wiki"),
        "created_by": film.get("created_by"),
        "cover": film.get("cover"),
        "comments": updated_comments
    }
    mongo.db.films.update({"_id": ObjectId(film_id)}, update)
    flash("Comment Successfully Deleted")
    return redirect(request.referrer)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=False)  # noqa: disable=line-too-long
