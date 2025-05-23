import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder="static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cocktails.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Cocktail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    image = db.Column(db.String(200), nullable=False)
    searches = db.Column(db.Integer, default=1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_ingredient', methods=['POST'])
def search_ingredient():
    ingredient = request.form.get('query')
    url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}"
    response = requests.get(url)

    drinks = response.json().get('drinks', []) if response.status_code == 200 else []

    return render_template('result_ingredient.html', ingredient=ingredient, drinks=drinks)


@app.route('/search_drink', methods=['POST'])
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


@app.route('/random_drink', methods=['GET'])
def random_drink():
    url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
    response = requests.get(url)

    drink = response.json().get('drinks', [])[0] if response.status_code == 200 else None

    return render_template('result_random.html', drink=drink)


@app.route('/top')
def top_drinks():
    top_drinks = Cocktail.query.order_by(Cocktail.searches.desc()).limit(10).all()
    return render_template('top_drinks.html', top_drinks=top_drinks)

@app.route('/impressum')
def impressum():
    return render_template('impressum.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)