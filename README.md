![screens](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/images/readMe_files/tiff_responsive.png?raw=true)

# Tiffany's Films Archive

This is the source code of the Tiffany's Films Archive. 

To see it in action just click this [link](https://omarbedawi.github.io/PizzeriaVecchiaMilano/).


## Goals
### Tiffany's Films Archive goals

The goal of this website is to easily display the user's collection and facilitate her to add, edit and delete films from the list in the home page.

### Target audience is:

* A films collector who was looking for an application to storage and have fast and easy access to its films informations.


### Business goals

* Interactive web-app
* Fully functional web app
* Intuitive design
* Easy to navigate


### Customer goals

* Find easy to access the collection and localize the desired films, typing in the search bar the film title or only one word of it. 
* Find easy to add a new film to the collection and eventually modify its information or delete the title from the collecion .


## Installation

In the head of the project I have installed the links to have access to different libraries. In the picture are wrapped in red.
![head](https://raw.githubusercontent.com/OmarBedawi/myMovies/master/static/images/readMe_files/1.header.png?raw=true)

1. Materialize: a library with templates for buttons, forms, sidenav and so many other components. For this project for example I used it to build the navigation bar, the search bar and the buttons.
1. Font Awesome: is an icon library. 
1. Cdnjs is a Javascript library and below the external link to the style.css file.
1. In the <head> of the orderonline page there is the link to connect to the sendEmailJs service.
  This service, every time an order is sent, make sure to send an email with the order to the pizzeria, and a confirmation email to the customer.
1. At the bottom of the page is where the javascript files are located. In every page html page for example there is the <script> to make the navbar responsive for every screen size. 
  
![javascript](https://raw.githubusercontent.com/OmarBedawi/PizzeriaVecchiaMilano/master/assets/images/readMe_files/2javascript_bottom.png?raw=true)



## User Stories

I built a responsive navbar, that shows a toggle menu when the screen size is below 991px. 
To build it I followed an accurate and guided tutorial that you can find at this [link](https://youtu.be/gt8zOLQ8A0w)

The homepage presents a carousel with pictures followed by the awards won by the pizzeria and a google map.

The menu page gives the possibility to see the pizza that you desire when you click on the button below every pizza: infact an image of the relative pizza, will appear.
Same thing happen with every dessert.

The ourstory page is telling a piece of history of the pizzeria. At the bottom of the page there is also a short video of the staff in action.

The gallery page is a collection of pictures shared by the pizzeria staff and the customers.

The order on-line page is for who want a home delivery or to pick up at the pizzeria.

The CSS file is divided by comments, that I used as title to separate the html pages or elements like map and carousel and the different screen sizes.

This make any future correction or research much easier.

![css](https://raw.githubusercontent.com/OmarBedawi/PizzeriaVecchiaMilano/master/assets/images/readMe_files/css_comments.png?raw=true)


![css2](https://raw.githubusercontent.com/OmarBedawi/PizzeriaVecchiaMilano/master/assets/images/readMe_files/css_screens.png?raw=true)





### WIREFRAMES

I built the wireframes using the [Balsamiq Cloud](https://balsamiq.cloud/) service.



![home](https://raw.githubusercontent.com/OmarBedawi/PizzeriaVecchiaMilano/master/assets/images/readMe_files/wireframes/1homepage.png?raw=true)
![menu](https://raw.githubusercontent.com/OmarBedawi/PizzeriaVecchiaMilano/master/assets/images/readMe_files/wireframes/2menu.png?raw=true)
![story](https://raw.githubusercontent.com/OmarBedawi/PizzeriaVecchiaMilano/master/assets/images/readMe_files/wireframes/3ourstory.png?raw=true)
![gallery](https://raw.githubusercontent.com/OmarBedawi/PizzeriaVecchiaMilano/master/assets/images/readMe_files/wireframes/4gallery.png?raw=true)
![order](https://raw.githubusercontent.com/OmarBedawi/PizzeriaVecchiaMilano/master/assets/images/readMe_files/wireframes/5orderon-line.png?raw=true)



## Technologies Used
### Languages
This project makes use of:
* [HTML] - base language for this project.
* [CSS] - Used for Styling the HTML code
* [JavaScript] - Used to make the web app interactive.
    
    
### Libraries    
* [Bootstrap](https://getbootstrap.com/) - Used for responsive navbar, for the menu page and the form.
* [JQuery](https://jquery.com/) - The project uses **JQuery** to simplify DOM manipulation.
* [FontAwseome](https://fontawesome.com/) - Used for all the icons on the site.
* [Google Fonts](https://fonts.google.com/) - Used for the 'Sansita Swashed' fonts.
* [Hover.css](https://ianlunn.github.io/Hover/) - Used to animate the social media icons.



### API

* [Emailjs](https://www.emailjs.com/) - Used to send the contact form in an email format to my gmail account.
* [Google Cloud Platform](https://console.cloud.google.com/) - Used to display a map provided from Google service, to show the pizzeria location.



### TOOLS

* [Google Chrome] - Used for browser and dev tools
* [Mozilla Firefox] - Used for browser and dev tools
* [Microsoft Edge] - Used for browser and dev tools
* [Google] - **Google** was used for research.
* [Balsamiq Cloud](https://balsamiq.cloud/) - Used for creation of wireframes.
* [Gitpod](https://www.gitpod.io/) - Used as IDE for this project.
* [Git](https://git-scm.com/) - Used for Version Control
* [GitHub](https://github.com/) - Used to host repository and live website.
* [Github Pages](https://pattern-projects.github.io/oireachtas-ifd-project/) - Website hosted on **Github Pages**
* [Am I Responsive](http://ami.responsivedesign.is/) - Used for testing purposes as well as creating the image to display the web pages on different devices.
* [W3 Html validator](https://validator.w3.org/) - Used to test and validate my html code.
* [W3 Css validator](https://jigsaw.w3.org/) - Used to test and validate my css code.
* [JSHint](https://jshint.com/) - Used to validate my Javascript code.
* [Color Scheme Designer](http://colorschemedesigner.com/) - Used to test colour combinations.
* [Free Formatter](https://www.freeformatter.com/) - Used to format my html, css and javascript code.
* [PageSpeed insights](https://developers.google.com/speed/pagespeed/insights/) - Used for testing the loading speed of the site.


![speedtest](https://raw.githubusercontent.com/OmarBedawi/PizzeriaVecchiaMilano/master/assets/images/readMe_files/speedtest.png?raw=true)
###### A caption of a speed test on PageSpeed insights.

## Testing

Navbar:
1. Go to any html page.
1. Try to reduce the screen size to any size below 991px and verify that a toggle menu appears on the top right angle of the screen.
1. Try to click on the toggle menu and verify that a list with all the pages of the website appears to you.
1. Try to click on every page provided by the toggle menu and verify that the pages are all connected between each other and reachable from any other page.
1. Try to hover the mouse over the Menu, Ourstory and Gallery links in the navbar and verify that their color text change to yellow and back to white when you move the mouse out.
1. Try to hover the mouse over the social media icons in the footer and verify that the icons color change to yellow and back to white when you move the mouse out.
1. Try to click on the social media icons and verify that they are correctly linked.
1. Try to click on the logo and verify that it redirect you to the "index" page.
1. Try to scroll any html page and verify that the navbar is fixed.


Carousel:
1. Go to the "index" page.
1. Click on the right arrow of the carousel and verify that the second image slide to the center of the carousel.
1. Click on the right arrow of the carousel and verify that the left arrow appears.
1. After the first click on the right arrow, click on left arrow to go back to the first picture, and verify that the left arrow disappears.
1. Click on the right arrow until you reach the last picture, and verify that the right arrow disappears.
1. Click on the dots right below the carousel and verify that every dot matches a picture.



Menu:
1. Go to the "menu" page.
1. Click on any button and verify that an image of the relative pizza or dessert will appear on  the page.
1. Click on any button and verify that the text "Show" on the button change in "Hide".

![menu1](https://raw.githubusercontent.com/OmarBedawi/PizzeriaVecchiaMilano/master/assets/images/readMe_files/menu1.png?raw=true)
![menu2](https://raw.githubusercontent.com/OmarBedawi/PizzeriaVecchiaMilano/master/assets/images/readMe_files/menu2.png?raw=true)




Video:
1. Go to the "our story" page.
1. Scroll to the end of the page where the video is placed, try to click on the "play" command and verify that the video is starting.


Gallery:
1. Go to the "gallery" page.
1. Set the size of the screen to at least 992px and verify that every raw has 4 columns of pictures.
1. Set the size of the screen between 576px and 992px and verify that every raw has 3 columns of pictures.
1. Set the size of the screen to less than 576px and verify that every raw has 2 columns of pictures.

![gall1](https://raw.githubusercontent.com/OmarBedawi/PizzeriaVecchiaMilano/master/assets/images/readMe_files/gall1.png?raw=true)
![gall2](https://raw.githubusercontent.com/OmarBedawi/PizzeriaVecchiaMilano/master/assets/images/readMe_files/gall2.png?raw=true)
![gall3](https://raw.githubusercontent.com/OmarBedawi/PizzeriaVecchiaMilano/master/assets/images/readMe_files/gall3.png?raw=true)


Contact form:
1. Go to the "Order on-line" page.
1. Try to submit the form with empty fields and verify that an error message about the required fields appears.
1. Try to submit the form with an invalid email address and verify that a relevant error message appears.
1. Try to submit the form with all inputs valid (and a valid email ) and verify that a confirmation email is sent to the email address provided.
1. Try to submit the form and verify that all the fields are cleared.


![email](https://raw.githubusercontent.com/OmarBedawi/PizzeriaVecchiaMilano/master/assets/images/readMe_files/email.png?raw=true)
###### Verify that the contact form information has been sent to my Gmail account by emailjs.


## Code Validation
* I used the [W3 Html validator](https://validator.w3.org/) service to validate my html code.

* I used the [W3 Css validator](https://jigsaw.w3.org/) service to validate my css code.

* I used the [JSHint](https://jshint.com/) service to validate my javascript code.




# Bugs

The project presents two little bugs that I still need to correct:

1. When the carousel is at last picture, the right arrow suppose to disappear but it doesn't.
1. Can't make the submit button to submit and clear the form at the same time. The two funtions for now, work only alternatively.























## Deployment

This web app was developed in Gitpod and pushed to the remote repository, GitHub. The live page is hosted on GitHub Pages.

### Used commands during deployment:

* git add . - to add the files to the staging area.
* git commit -m "text message here" - to commit the files.
* git push - to push to origin master branch on to GitHub.
* git status - to see the current status of the files.

### Hosting on GitHub Pages

* Log into GitHub.
* From the list of repositories choose [PizzeriaVecchiaMilano](https://github.com/OmarBedawi/PizzeriaVecchiaMilano).
* Go to settings.
* Scroll down to GitHub Pages section.
* Select as a source master branch.
* The page is now automatically refreshed and the project is deployed.
* To access the project scroll down again to GitHub Pages section and click on the provided link.

For more detailed information regarding deployment to GitHub Pages click [here](https://pages.github.com/).

### How to run this project locally
#### Clone this project from GitHub:

* Go to [PizzeriaVecchiaMilano](https://github.com/OmarBedawi/PizzeriaVecchiaMilano) GitHub repository.
* Click on "Clone or download" green button.
* Copy the URL to the repository.
* Open the terminal in your IDE.
* Choose the working directory where you would like to have the cloned repository.
* Type git clone, and add the URL you copied from Github: git clone https://github.com/OmarBedawi/PizzeriaVecchiaMilano-Web-App.git
* Press Enter and your local clone will be created.

For more information regarding cloning of a repository click here.

### Acknowledgements
Thank you to the following for inspiration, motivation and the direction I needed:

- Seun Owonikoko   (my mentor)
- Code Institute staff

## Disclaimer

This web page was created for educational purposes only.
