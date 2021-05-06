# Film's Archive Application


![screens](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/screenshots/film_responsive.png?raw=true)



This is the source code of the Film's Archive Application. 

To see it in action just click this [link](http://my-first-heroku-for-movies.herokuapp.com/).


## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the main purpose of the site.
        2. As a First Time Visitor, I want to be able to easily navigate throughout the application to find content.
        3. As a First Time Visitor, I want to easily be able to add new films to the collection.
        

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to have easy and fast access to the film's informations.
        2. As a Returning Visitor, I want to easily be able to filter one or more specific film title that I'm looking for.
        3. As a Returning Visitor, I want to easily be able to update or cancel an exsisting record.

    -   #### Frequent User Goals
        1. As a Frequent User, I want to check if there are any newly added function or content.
        2. As a Frequent User, I want to check if there are any new options to manipulate the record information.
        
-   ### Design
    -   #### Colour Scheme
        -   The two main colours used are blue, and light grey.
    
    -   #### Imagery
        -   Imagery is important. The background image with all the film covers is designed to be striking and catch the user's attention and let him understand what is the topic of the website. 


*   ### Wireframes


The wireframes information can be found [here](static/readMe_files/wireframes/wireframe.md).


## Features
### Existing Features
* #### Dynamic Search Bar 
    * Films can be searched or filtered by title using the search bar.
    * User need to type at least one word contained in the film's title.
    * Number of results for searches is dynamically displayed on top of the page, just before the list of films.

* #### Cards Reveal
    * Each film is contained in a reveal card, that is a card with front and back side.
    * The front side shows a cover picture of the film followed by the title, the year and a link to direct the user to the wikipedia page of the film.
    * The title can occupy only one line. If it is longer it will be truncate. If the wikipedia link is not added a short paragraph will say "Link Not Added".
    * At the bottom of the card, if the film has been added by the user, the "edit" and "delete" buttons are displayed. If the film is added by another user, it will show the username of that user.
    * The back side of the card is accessable by clicking on the image on the front side.
    * The back side displays the full film's title and a comment section, where all the users can leave comment and opinion about that specific film.

* #### User Profile
    * User have to create a profile, in order to be able to access the application.

* #### Flash Messages 
    * Throughout the site flash messages are used to give the user feedback, such as 
    when a user logs in, logs out, adds, edit or delete a film.

* #### Responsive Fixed Navbar
    * The Navbar is fixed and always attached to the top of the page.
    * When the screen size is less than 992px, a toggle menu appears on the top right corner of the screen.
    * When the toggle is clicked, a sideNav appears on the right side of the page and displays the links to access the other pages of the site. 
    * Logo text is always available on the top left corner. If clicked, redirects the user to the My Films page.
  
### Features Left to Implement
* #### Star System Rating
    * With more time, a nice 5 stars system rating will be added in the comment section.

* #### Custom 404 Page 
    * Fairly self explanatory, but this feature wasn't deemed necessary for the site to be deployed.
  
## Technologies Used

### Languages Used

This project makes use of:
* [HTML] - Base language for this project.
* [CSS] - Used for Styling the HTML code
* [JavaScript] - Used to make the web app interactive.
* [Python](https://www.python.org) - Used to build the functions of every html page
* [Mongo DB](https://www.mongodb.com) - Mongo DB is a document-oriented database program. Used to store all the films and users of the application.
* [Jinja Template](https://jinja.palletsprojects.com/) - Jinja is a web template engine for the Python programming language


### Libraries    
* [Materialize](https://materializecss.com/) - Used for responsive navbar, forms, buttons and collapsibles.
* [JQuery](https://jquery.com/) - The project uses **JQuery** to simplify DOM manipulation.
* [FontAwseome](https://fontawesome.com/) - Used for all the icons in the application.


### API

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Used to have more control and better interaction with the databases.


### TOOLS

* [Google Chrome] - Used for browser and dev tools
* [Mozilla Firefox] - Used for browser and dev tools
* [Microsoft Edge] - Used for browser and dev tools
* [Google] - **Google** was used for research.
* [Balsamiq Cloud](https://balsamiq.cloud/) - Used for creation of wireframes.
* [Gitpod](https://www.gitpod.io/) - Used as IDE for this project.
* [Git](https://git-scm.com/) - Used for Version Control
* [GitHub](https://github.com/) - Used to host repository and live website.
* [Heroku](https://www.heroku.com) - Heroku is a container-based cloud Platform. Used to deploy the application and create the domain.
* [Am I Responsive](http://ami.responsivedesign.is/) - Used for testing purposes as well as creating the image to display the web pages on different devices.
* [W3 Html validator](https://validator.w3.org/) - Used to test and validate my html code.
* [W3 Css validator](https://jigsaw.w3.org/) - Used to test and validate my css code.
* [JSHint](https://jshint.com/) - Used to validate my Javascript code.
* [Color Scheme Designer](http://colorschemedesigner.com/) - Used to test colour combinations.
* [Free Formatter](https://www.freeformatter.com/) - Used to format my html, css and javascript code.
* [Python Formatter](https://codebeautify.org/python-formatter-beautifier) - Used to format my python files
* [PageSpeed insights](https://developers.google.com/speed/pagespeed/insights/) - Used for testing the loading speed of the site.


![speedtest](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/screenshots/speed_test.png?raw=true)
###### A caption of a speed test on PageSpeed insights.


## Testing

Testing information can be found [here](static/readMe_files/testing/testing.md).


## Code Validation
* I used the [W3 Html validator](https://validator.w3.org/) service to validate my html code.

    -   #### All html files passes succesfully through the 'check by address' validator.
    -   #### The "my_film.html" file has been validate by the source code of the page.

* I used the [W3 Css validator](https://jigsaw.w3.org/) service to validate my Css code.

* I used the [JSHint](https://jshint.com/) service to validate my JavaScript code.


### Known Bugs

-   The console is displaying an Error 404 (favicon.ico:1) but after a deep research I can't understand what the error is about. However, this error is not interfering with the functionality of the code.

## Deployment

This web app was developed in Gitpod and deployed to the remote repository, Heroku. 

### Used commands during committing in Gitpod:

* git add -A - to add the files to the staging area.
* git commit -m "text message here" - to commit the files.
* git push - to push to origin master branch on to GitHub.
* git status - to see the current status of the files.

### Heroku Pages

The project was deployed to Heroku Pages with the following steps:

1. Create a requirements.txt file using the terminal command pip freeze > requirements.txt
2. Create a Procfile with the terminal command echo web: python app.py > Procfile
3. Git add and git commit the new requirements and Procfile and then git push the project to GitHub
4. Create a new app on the Heroku website by clicking the "New" button in your dashboard. Give it a name and set the region to Europe
5. From the Heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub
6. Confirm the linking of the Heroku app to the correct GitHub repository
7. In the Heroku dashboard for the application, click on "Setting" > "Reveal Config Vars"
8. In the "Reveal Config Vars" set IP, MONGO_URI, PORT and SECRET_KEY.


To locate the link project use the following steps:

1. Log in to Heroku and choose [myMovies](https://dashboard.heroku.com/apps/my-first-heroku-for-movies).
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
3. Scroll down the Settings page until you locate the "Domains" Section.
4. On the right side of the page you can find the project [link](http://my-first-heroku-for-movies.herokuapp.com/).

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and choose [myMovies](https://github.com/OmarBedawi/myMovies).
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and choose [myMovies](https://github.com/OmarBedawi/myMovies).
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.
7. Press Enter. Your local clone will be created.

## Credits
### Content

-   All content was written by the developer.


### Media

-   All Images in the readMe file were created by the developer.

### Acknowledgements

-   My Mentor Antonio Rodriguez for continuous helpful feedback.

-   Tutor support at Code Institute for their support.

