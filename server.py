"""Models and database functions for Foodio"""

#import library & modules & files
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db

# create flask app
app = Flask(__name__)

# create secret key, necessary for sessions:
app.secret_key = 'hj8fal15iz3d0fx8fN0abi6bf'
