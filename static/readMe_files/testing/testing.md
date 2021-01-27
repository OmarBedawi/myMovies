[back to README.md file](https://github.com/OmarBedawi/myMovies/blob/master/README.md)


# Testing


Navbar and Links:
1. Go to the Home page.
1. To make sure that no profile is logged in, verify that the only 3 links available on the navbar are "Home", "Log In" and "Register".
1. Try to reduce the screen size to any size below 991px and verify that a toggle menu appears on the top right corner of the screen.
1. Try to click on the toggle menu and verify that a mobile side nav appears to you with all the links.
1. Try to click on the logo and verify that it redirect you to the Home page.
1. Try to scroll any html page and verify that the navbar is fixed.

1)



Login, Register and Profile pages:
1. Go to the "Register" page, create your username and password: if the username is already in the database the following flash message will appear "Username already exists".
   Otherwise make sure the flash message "Registration Successful" will be display and you directed to the "Profile" page.
1. From the "Profile" page, try to click on the "Log Out" link and make sure the flash message displayed is "You have been logged out" and directed to the "Log In" page.
1. From the "Log In" page try to click the link "Register Account" below the form, and verify that you are directed to the "Register" page.
1. From the "Register" page try to click the link "Log In" below the form, and verify that you are directed to the "Log In" page.
1. From the "Log In" page try to login with a random username and password and verify the following flash message: "Incorrect Username and/or Password"
1. From the "Log In" page try to login with the correct username and password and verify that the flash message "Welcome (username)" is displayed on the "Profile" page.

2)
3)
4)
5
6
7


Add Film page:
1. Go to the "Add Film" page.
1. Try to submit the form with at least one of the label marked with the red asteriks empty, and verify that an error message about the required fields appears.
1. Try to submit the form with all the required fields filled out, and verify to be redirect to the "Home" page with the flash message of "Film Successfully Added".


8)
9)
10)
 

Home page:
1. Try to find the film added by you, and verify that the buttons "Delete" and "Edit" are displeyed.
2. Try to click on the "Edit" button and verify that the "Edit Film" page is displayed and allows you to modify any information about the film.
3. Try to click on the button "Edit Film" and verify the following flash message "Film Successfully Updated" and be redirected to the "Home" page.

11)
12)
13)


1. Try to click on the "Delete" button and verify that a confirmation message asking "Are you sure to delete this film?" is displayed.
   Try to click "yes" and verify that the flash message "Film Successfully Deleted" is displayed.
   
14)
15)


The search bar:
1. Try to click on the "Search" button without to type anything in the search bar and verify that an error message about the required fields appears.
1. Try to type in the search a bar a random film that not even exist or not present in the list and verify that the flash message "No Results Found" is displayed.
1. Try to click on the "Reset" button and verify that the list of films is restored again in the "Home" page.









   
   
   
   
   
   

