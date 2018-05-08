"""Models and database functions for Foodio"""

#import library & modules & files
from flask import Flask, session, render_template, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Food, Refrigerator, Recipe

from jinja2 import StrictUndefined

# create flask app
app = Flask(__name__)

# create secret key, necessary for sessions:
app.secret_key = 'hj8fal15iz3d0fx8fN0abi6bf'

# raises jinja underfined error 
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():

        return render_template('homepage.html')


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

@app.route('/user-<user_id>')
def display_homepage(user_id):
    """Show user's information"""
    print 'homepage', user_id

    user_refrigerator = (Refrigerator.query.filter_by(user_id = user_id)).all()
    print user_refrigerator

    return render_template('user-home.html', user_refrigerator=user_refrigerator)


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


@app.route('/logout')
def logout():
    session.pop('user')
    flash('You were successfully logged out')

    return redirect('/')
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
