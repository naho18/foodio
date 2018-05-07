"""Models and database functions for Foodio"""

#import library & modules & files
from flask import Flask, session, render_template, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db

# create flask app
app = Flask(__name__)

# create secret key, necessary for sessions:
app.secret_key = 'hj8fal15iz3d0fx8fN0abi6bf'


@app.route('/')
def index():

        return render_template('homepage.html')



@app.route('/login', methods=['POST'])
def login_check():
    """Validates user info"""

    # Get user email & password from form
    user_email = request.form['email']
    user_password = request.form['password']

    # Check user info against database
    email_query = User.query.filter_by(email=user_email).first()
    if email_query == None:
        flash('')

@app.route('/registration')
def register_user():
    """Registers user"""

    return render_template('homepage.html')

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
    app.run()
