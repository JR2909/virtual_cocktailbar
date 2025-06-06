import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder="static") #create object of class Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cocktails.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) # create object of class SQLAlchemy

class Cocktail(db.Model): # declare class Cocktail
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    image = db.Column(db.String(200), nullable=False)
    searches = db.Column(db.Integer, default=1)

@app.route('/')
def index():
    return render_template('index.html')
#approute for homepage

@app.route('/search_ingredient', methods=['POST']) # should be GET-Method, but returns an error, so POST Method used
def search_ingredient():
    ingredient = request.form.get('query')
    url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}"
    response = requests.get(url)

    drinks = response.json().get('drinks', []) if response.status_code == 200 else []

    return render_template('result_ingredient.html', ingredient=ingredient, drinks=drinks)
# search function for ingredients via api

@app.route('/search_drink', methods=['POST']) # should be GET-Method, but returns an error, so POST Method used
def search_drink():
    drink_name = request.form.get('query')
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink_name}"
    response = requests.get(url)

    drinks = response.json().get('drinks', []) if response.status_code == 200 else []

    if drinks:
        for drink in drinks:
            existing_drink = Cocktail.query.filter_by(name=drink['strDrink']).first()
            if existing_drink:
                existing_drink.searches += 1
            else:
                new_drink = Cocktail(
                    name=drink['strDrink'],
                    image=drink['strDrinkThumb'],
                    searches=1
                )
                db.session.add(new_drink)

            db.session.commit()

    return render_template('result_drink.html', drink_name=drink_name, drinks=drinks)
# search function for drinks via api and adding them to the database for the top 10 drinks

@app.route('/random_drink', methods=['GET'])
def random_drink():
    url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
    response = requests.get(url)

    drink = response.json().get('drinks', [])[0] if response.status_code == 200 else None

    return render_template('result_random.html', drink=drink)
# search function for random drinks via api

@app.route('/top')
def top_drinks():
    top_drinks = Cocktail.query.order_by(Cocktail.searches.desc()).limit(10).all()
    return render_template('top_drinks.html', top_drinks=top_drinks)
# list of the top drinks, via the database in instances/cocktail.db

@app.route('/impressum')
def impressum():
    return render_template('impressum.html')
# route for the impressum

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
# route for the errorhandler

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
