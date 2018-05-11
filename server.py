"""Models and database functions for Foodio"""

#import library & modules & files
from flask import Flask, session, render_template, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Food, Refrigerator, Recipe

from datetime import datetime
from jinja2 import StrictUndefined

import unirest
import os

# create flask app
app = Flask(__name__)

# create secret key, necessary for sessions:
app.secret_key = 'hj8fal15iz3d0fx8fN0abi6bf'

# raises jinja underfined error
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():

        return render_template('homepage.html')


@app.route('/registration', methods=['POST'])
def register_user():
    """Registers user"""

    user_name = request.form['name']
    user_email = request.form['email']
    user_password = request.form['password']

    # Check to see if user already exists
    email_query = User.query.filter_by(email=user_email).all()

    if email_query:
        flash('Already a member. Please log in')
        return redirect('/')
    else:
        # Add user to database
        user = User(name=user_name, email=user_email, password=user_password)
        db.session.add(user)
        db.session.commit()

        flash('Registration successful! Please log in!')
        return redirect('/')


@app.route('/login', methods=['POST'])
def login_check():
    """Validates user info, takes user to home page"""

    # Get user email & password from form
    user_email = request.form['email']
    user_password = request.form['password']

    # Check user info against database
    email_query = User.query.filter_by(email=user_email).first()
    if email_query == None:
        flash('Invalid email')
        return redirect('/')

    # Get user's id using email
    user_id = email_query.user_id
    print user_id

    # Valid user password
    password_query = User.query.filter_by(password=user_password).all()

    if user_password == email_query.password:
        #create user session
        session['user'] = email_query.user_id
        flash('You are successfully logged in!')
        return redirect('/user-%s' % user_id)
    else:
        flash('Invalid password')
        return redirect('/')


@app.route('/logout')
def logout():
    session.pop('user')
    flash('You were successfully logged out')

    return redirect('/')


@app.route('/user-<user_id>')
def display_homepage(user_id):
    """Show user's information"""
    print 'homepage', user_id

    user_refrigerator = (Refrigerator.query.filter_by(user_id = user_id)).all()
    print user_refrigerator

    return render_template('user-home.html', user_id=user_id, user_refrigerator=user_refrigerator)


@app.route('/add-food', methods=['POST'])
def add_food():
    """Adds ingredient to Food database, adds refrigerator"""

    ingredient = request.form['ingredient']
    quantity_input = request.form['quantity']
    quantity = int(quantity_input)
    added_on = str(datetime.now())

    # look into calendar display to click on date
    # expires = request.args.get('expires')
    # expires_on = 

    # get user_id from form
    user_id = request.form['user_id']
    print user_id 

    food = Food(food=ingredient, quantity=quantity, added_on=str(datetime.now()))
    db.session.add(food)
    db.session.commit()

    # get food_id
    food_id = food.food_id
    print food.food_id

    refrigerator = Refrigerator(user_id=user_id, food_id=food_id)
    db.session.add(refrigerator)
    db.session.commit()

    # user_refrigerator = (Refrigerator.query.filter_by(user_id = user_id)).all()

    flash('item successfully added!')

    #return user_id & food_id to add-refrigerator

    # return render_template('user-home.html', user_id=user_id, user_refrigerator=user_refrigerator)
    return redirect('/user-%s' % user_id)


@app.route('/remove-food', methods=['POST'])
def remove_food():
    """Removes ingredient from Food database"""
    # http://docs.sqlalchemy.org/en/latest/orm/query.html?
    # http://flask-sqlalchemy.pocoo.org/2.3/queries/

    user_id = request.form['user_id']
    food_id = request.form['rm-ingredient']

    # query to delete refrigerator by user_id & food_id from Refrigerator table
    del_fridge = Refrigerator.query.filter(
        Refrigerator.user_id == user_id, Refrigerator.food_id == food_id).delete()

    db.session.commit()

    # query to delete food by food_id from Food table

    del_food = Food.query.filter(Food.food_id == food_id).delete()
    db.session.commit()

    # db.session.add_delete([del_food, del_fridge])

    return redirect('/user-%s' % user_id)


@app.route('/recipes')
def display_recipes():
    """Find recipes using Spoonacular API"""

    user_id = 2
    user_refrigerator = (Refrigerator.query.filter_by(user_id = user_id)).all()
    ingredients = ""

    # create ingredients list to pass to API request
    for item in user_refrigerator:
        print item.food.food
        ingredients += item.food.food + ", "

    # payload = {'fillIngredients': 'false', 'ingredients': ingredients, 'limitLicense': 'false', 'number':6, 'ranking':1}

    # r = unirest.get(
    #     "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients", 
    #     headers={"X-Mashape-Key": os.environ['X_Mashape_Key'],
    #     "Accept": "application/json"}, params=payload
    # )
    # #r = object
    #response list of dictionaries

    # entire body (all 6 recipes) 
    # body = r.body
    # body[0] first recipe
    # title --> title = body[0]['title']
    
    # print body
    # print title

    body = [
    {u'title': u'Fried Shrimp Rolls', u'image': u'https://spoonacular.com/recipeImages/743121-312x231.jpeg', 
    u'missedIngredientCount': 9, u'likes': 97, u'usedIngredientCount': 4, u'id': 743121, u'imageType': u'jpeg'}, 

    {u'title': u'Salmon Burger with Dill/Caper Tartar Sauce and Red Onion Ceviche', u'image': u'https://spoonacular.com/recipeImages/767322-312x231.jpg', 
    u'missedIngredientCount': 12, u'likes': 0, u'usedIngredientCount': 4, u'id': 767322, u'imageType': u'jpg'}, 

    {u'title': u'Green Goddess Salmon Burgers', u'image': u'https://spoonacular.com/recipeImages/880658-312x231.jpg', u'missedIngredientCount': 15, u'likes': 0, 
    u'usedIngredientCount': 4, u'id': 880658, u'imageType': u'jpg'}, 

    {u'title': u"Seafood Po' Boy with Umami Remoulade", u'image': u'https://spoonacular.com/recipeImages/770137-312x231.jpeg', u'missedIngredientCount': 17, u'likes': 4, u'usedIngredientCount': 4, u'id': 770137, u'imageType': u'jpeg'}, 

    {u'title': u'Zesty Salmon Burgers with Dill Spread', u'image': u'https://spoonacular.com/recipeImages/595943-312x231.jpg', u'missedIngredientCount': 20, u'likes': 674, u'usedIngredientCount': 4, u'id': 595943, u'imageType': u'jpg'}, 

    {u'title': u'Smoked Salmon & Scrambled Eggs Recipe', u'image': u'https://spoonacular.com/recipeImages/78568-312x231.jpg', u'missedIngredientCount': 2, u'likes': 121, u'usedIngredientCount': 3, u'id': 78568, u'imageType': u'jpg'}]

    return render_template("recipes.html",
                           body=body)


##############################################################################


@app.route('/test')
def testing():
    """Show test page"""

    users = User.query.all()

    return render_template('testing.html', users=users)
if __name__ == "__main__":
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    DebugToolbarExtension(app)
    connect_to_db(app)
    app.run('0.0.0.0')
