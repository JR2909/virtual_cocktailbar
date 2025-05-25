# Virtual Cocktailbar

## requirements.txt
Textfile, that shows the needed packages and their versions on the developed device. Other versions may be compatible to. 

## app.py
Script, that works as the backbone of the website.
The script imports the packages requests, from the package flask the elements Flask, render_template, request and from the package flask-sqlalchemy the class SQLAlchemy. The scipt creates the object app, an instance of Flask and after a few configurations the object db, an instance of SQLAlchemy. Then the class Cocktail is defined, inheriting the features of db.model. After that the following functions are defined. If the script is run, a database is created and the app will run on 127.0.0.1:5000

### app.py/index
Function that renders the page templates/index.html with the approute "/"

### app.py/search_ingredient
Function, searches for an ingredient in a cocktail via the api https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}. The ingredient is received via the query with the id "ingredient" in index.html and forwarded to the template result_ingredient.html with the approut "/search_ingredient"

### app.py/search_drink
Function, that searches for a particular drink by its name, e.g. Moscow Mule or Negroni via the api https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink_name}. <br>
After that the function will check, if the coctail exists in instance/cocktail.db

### app.py/random_drink
The function sends a GET request at https://www.thecocktaildb.com/api/json/v1/1/random.php. The output will be returned as a json and forwareded to the teplates/result_random.html. The function has the approut "/random_drink"

### app.py/top_drinks
The function will call the top 10 drinks from instance/cocktails.db and forward them to templates/top_drinks.html with the approute "/top"

### app.py/impressum
Function that renders the page templates/impressum.html with the approute "/impressum"

### app.py/page_not_found
Errorhandler for 404 Errors, renders 404.html

## templates/base.html
This file contains the code for the navbar, including the navigation to the other files, templates/index.html as "Home", templates/top.html as Top Drinks and templates/impressum.html as Impressum. The Navbar also contains the icon for changing between light and darkmode, in the top left corner

## templates/index.html
This file contains the homepage of the website, including a container with the videos from static/videos/.. as a background and the text "Welcome to the virtual 🍹 Cocktailbar 🍸". Below the container are three boxes, the first contains an input box, where an ingredient can be put and sent to the api, mentioned in app.py/search_ingredient. As a return you recive a list of cocktails with this specific ingredients on templates/result_ingredients.html. 

## templates/top_drinks.html
This files contains the code for the website with the approut "/top". It contains a list, with the top 10 drinks, searched via the function in "templates/app.py/search_drink" and saved in "instances/cocktail.db". The cocktails are displayed in a table, with the columns Rank, Cocktail Name, Image, Search Count. 

## templates/impressum.html
This file contains the code for the ipressum with the nessecarry legal information for a website.

## templates/result_drink.html
This file contains the code for a table that displays the results, recived in a json file from https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink_name}, as a table with the columns Name, Image, Ingredients and Instructions. 

## templates/result_ingredients.html
This file contains, same as templates/result_drink.html, the code for a table to display the input, recived in a json file from https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}, with the columns Name, Image, Recipe

## templates/result_random.html
The file contains the code to display a random cocktail recived via https://www.thecocktaildb.com/api/json/v1/1/random.php.

## templates/404.html
HTML-Page that works as errorhandler, shown when the error 404 occurs 

## static/scripts.js
This File contains the scripts for the website. <br>
The first function clears the inputfields after sending a request for an ingredient or a drink. <br>
The second function contains the code to activate or deactivate the darkmode and stores the status of the darkmode, so it will be applied to all pages. 
The thrid function renders and loops the seven videos in static/videos/.. for the background of the text "Welcome to the virtual 🍹 Cocktailbar 🍸" on templates/index.html

## static/styles.css


## static/moon-icon.jpg
The icon for activating the darkmode, referenced in templates/base.html

## static/treasure-chest.jpg
The picutre shown in the page of the errorhandler, templates/404.html

## static/ingredients.jpg
Picture shown in the box ingredients, in templates/index.html, for entertainment purpose

## static/drink.jpg
Picture shown in the box drink, in templates/index.html, for entertainment purpose

## static/random_drink.png
Picture shown in the box random_drink, in templates/index.html, for entertainment purpose

## static/videos/...
Contains the videos used for the video background in templates/index.html. 

## instance/cocktails.db
The database, created with flask-sqlalchemy and used to show the to searched cocktails. The database is referneced in templates/top_drinks.html
