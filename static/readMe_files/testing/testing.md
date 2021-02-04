[back to README.md file](https://github.com/OmarBedawi/myMovies/blob/master/README.md)


# Testing


### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the site.

        1. Upon entering the site, users are automatically greeted with a clean and easily readable navigation bar (or sidenav for screens smaller than 991px) to go to the page of their choice. Underneath there is a collapsible that is framed with a shade of green to immediately catch the eye of the user. Clicking on the collapsible will expand an area where the user can find some basic instructions about the porpose and how to use the application.
        2. The main points are made immediately with the framed collapsible.
        3. The user has two options, scroll down and click the link underneath the form or click the link in the navigation bar, both will lead to the same place, to create an account and be able to access the application.

    2. As a First Time Visitor, I want to be able to easily navigate throughout the application to find content.

        1. The site has been designed to be fluid and never to entrap the user. At the top of each page there is a clean navigation bar, each link describes what the page they will end up at clearly.
        2. When the visitor is logged in, clicking the logo is always directing the user to the collection/home page.    
        3. The search bar in the home page gives the user the opportunity to filter records.
        
    3. As a First Time Visitor, I want to easily be able to add new records.
        1. Once the visitor access the site with a username, the user can easily find the link "Add Film" in the navigation bar and start to compose his collection.
        2. On the "Add Film" Page, after the form response is submitted, the page refreshes and the user is brought to his collection/home page and a flash message on the top of the page is displayed and saying: "Film Successfully Added".
        

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to have easy and fast access to the record's informations.

        1. Once the visitor is logged in, he only need to click on a collapsible-header that contain a record and the expandable area will display the hidden informations of that record.
        2. If the visitor needs to find a specific record in a long list, he can use the search bar to filter his research and access the desire record.

    2. As a Returning Visitor, I want to easily be able to filter a specific record that I'm searching.

        1. Once the visitor is logged in, on the top of the collection page the user can find the search bar as first content available.
        2. The search bar is the perfect tool to filter the user research. The research could be based on the title, or only one word contained in it.

    3. As a Returning Visitor, I want to find the Facebook Group link so that I can join and interact with others in the community.
    3. As a Returning Visitor, I want to easily be able to update or cancel an exsisting record.
        1. In the collection page, every record is displayed with 2 buttons: edit and delete. 
        2. The edit button direct the user to the "Edit Film" page. Here the user has the opportunity update the informations contained in the record.
        3. After the form response is submitted, the page refreshes and the user is brought to his collection/home page and a flash message on the top of the page is displayed and saying: "Film Successfully Updated".
        4. The delete button gives the user the opportunity to delete a record. When the user click on the button, a message appear on  the screen saying:"Are you sure to delete this film?"
        If the user click "Yes", a flash message on the top of the page is displayed and saying: "Film Successfully Deleted". 

-   #### Frequent User Goals

    
    1. As a Frequent User, I want to check to see if there are any newly added function or content.

        1. The user would already be comfortable with the website layout.

    2. As a Frequent User, I want to check to see if there are any more options to manipulate the record information.

        1. The user would already be comfortable with the website layout and can easily click the blog link

    

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Navbar and Links:
1. Go to the Home page.
1. To make sure that no profile is logged in, verify that the only 3 links available on the navbar or the sidenav are "Home", "Log In" and "Register".
1. Try to reduce the screen size to any size below 991px and verify that a toggle menu appears on the top right corner of the screen.
1. Try to click on the toggle menu and verify that a mobile side nav appears to you with all the links.
1. Try to click on the logo and verify that it redirect you to the "Home" page.
1. Try to scroll any html page and verify that the navbar is fixed.


![Test 01](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/01_home_out.png?raw=true)



Login, Register and Profile pages:
1. Go to the "Register" page, create your username and password: if the username is already in the database the following flash message will appear on the screen: "Username already exists".
   In the moment you create a valid profile, verify the flash message "Registration Successful" will be display and you directed to the "Profile" page.
1. From the "Profile" page, try to click on the "Log Out" link and make sure the flash message displayed is "You have been logged out" and directed to the "Log In" page.
1. From the "Log In" page try to click the link "Register Account" below the form, and verify that you are directed to the "Register" page.
1. From the "Register" page try to click the link "Log In" below the form, and verify that you are directed to the "Log In" page.
1. From the "Log In" page try to login with a random username and password and verify the following flash message: "Incorrect Username and/or Password"
1. From the "Log In" page try to login with the correct username and password and verify that the flash message "Welcome (username)" is displayed on the "Profile" page.


![Test 02](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/02_user_exist.png?raw=true)



![Test 03](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/03_registered.png?raw=true)



![Test 04](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/04_log_out.png?raw=true)



![Test 05](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/05_register.png?raw=true)



![Test 06](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/06_incorrect_login.png?raw=true)



![Test 07](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/07_logged_in.png?raw=true)



Add Film page:
1. Go to the "Add Film" page.
1. Try to submit the form and keep empty at least one of the label marked with the red asteriks, and verify that an error message about the required fields appears.
1. Try to submit the form with all the required fields filled out, and verify to be redirect to the "Home" page with the flash message of "Film Successfully Added".



![Test 08](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/08_add_film_label.png?raw=true)



![Test 09](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/09_add_film_label2.png?raw=true)



![Test 10](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/10_added.png?raw=true)



Home page:
1. Try to find the film added by you, and verify that the buttons "Delete" and "Edit" are displeyed.
2. Try to click on the "Edit" button and verify that the "Edit Film" page is displayed and allows you to modify any information about the film.
3. Try to click on the button "Edit Film" and verify the following flash message "Film Successfully Updated" and be directed to the "Home" page.
4. Try to click on any collapsible and verify that his area it expands and shows the additional informations contained.



![Test 11](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/11_home_in.png?raw=true)



![Test 12](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/12_editing.png?raw=true)



![Test 13](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/13_edit.png?raw=true)



![Test 14](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/14_expand.png?raw=true)



1. Try to click on the "Delete" button and verify that a confirmation message asking "Are you sure to delete this film?" is displayed.
   Try to click "yes" and verify that the flash message "Film Successfully Deleted" is displayed.
   
   
   
![Test 15](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/15_delete.png?raw=true)



![Test 16](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/16_deleted.png?raw=true)



The search bar:
1. Try to click on the "Search" button without to type anything in the search bar and verify that an error message about the required fields appears.
1. Try to type in the search a bar a random film that not even exist or not present in the list and verify that the flash message "No Results Found" is displayed.
1. Try to click on the "Reset" button and verify that the list of films is restored.



![Test 17](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/17_search_required.png?raw=true)



![Test 18](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/18_no_result.png?raw=true)



1. Try to type one word that is contained in one or more film title, and verify that all the films with that specific word in the title are filtered and displayed. 
1. Try to type the whole title of a film and verify that the specific film is diplayed



![Test 19](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/19_search_word.png?raw=true)



![Test 20](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/20_search_title.png?raw=true)
   


1. Try to reduce the screen at the width of 400px and verify that the "Reset" and "Search" buttons are moved below the search bar and the "Delete" and "Edit" buttons are moved 
one row below to give space, in case a title is too long.



![Test 21](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/readMe_files/testing/testing_screenshots/21_mobile_size.png?raw=true)
