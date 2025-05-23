# Virtual Cocktailbar

## app.py
Script, that works as the backbone of the website. 
### app.py/index
Function that renders the page templates/index.html with the approute "/"

### app.py/search_ingredient
Function, that searches for an ingredient in a cocktail via the api https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}. The ingredient is received via the query with the id "ingredient" in index.html and forwarded to the template result_ingredient.html 

### app.py/search_drink
Function, that searches for a particular drink by its name, e.g. Moscow Mule or Negroni via the api https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink_name}. <br>
After that the function will check, if the coctail exists in instance/cocktail.db


### app.py/random_drink


### app.py/top_drinks


### app.py/impressum
Function that renders the page templates/impressum.html with the approute "/impressum"

### app.py/page_not_found
Errorhandler for 404 Errors, renders 404.html

## templates/base.html

## templates/index.html

## templates/top_drinks.html

## templates/impressum-html

## templates/result_drink.html

## templates/result_ingredients.html

## templates/result_random.html

## static/scripts.js

## static/styles.css

## static/moon-icon.jpg
The icon for activating the darkmode, referenced in templates/base.html

## static/videos/...
Contains the videos used for the video background in index.html. 

## instance/cocktails.db
The database, created with flask-sqlalchemy and used to show the to searched cocktails. The database is referneced in templates/top_drinks.html
