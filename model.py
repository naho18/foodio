"""Models and database functions for Foodio"""

#import library
from flask_sqlalchemy import SQLAlchemy

#create database
db = SQLAlchemy()

##############################################################################
# create model for each table


class User(db.Model):
    """User of Foodio"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        """Show information about users"""

        return "<user_id= %s name= %s>" % (self.user_id, self.name)


class Food(db.Model):
    """Ingredients stored in refrigerators"""

    __tablename__ = "foods"

    food_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer)
    added_on = db.Column(db.DateTime)
    expires_on = db.Column(db.DateTime)

    def __repr__(self):
        """Show information about food in refrigerator"""

        return "<food_id= %s food= %s quantity= %d>" % (
            self.food_id, self.food, self.quantity)


class Refrigerator(db.Model):
    """Users' refrigerators"""

    __tablename__ = "refrigerators"

    refrigerator_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('foods.food_id'), nullable=False)

    # create relationship with User and Food tables
    user = db.relationship('User', backref='refrigerators')
    food = db.relationship('Food', backref='refrigerators')

    def __repr__(self):
        """Shows information about refrigerators"""

        return "<refrigerator_id= %d user_id= %d food_id= %d>" % (
            self.refrigerator_id, self.user_id, self.food_id)


class Recipe(db.Model):
    """Users' favorited recipes"""

    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    title = db.Column(db.String(256), nullable=False)
    url = db.Column(db.String(256), nullable=False)
    img = db.Column(db.String(256), nullable=False)

    #create relationship with User table
    user = db.relationship('User', backref='recipes')

##############################################################################
# create helper functions


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///foodio'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # connect db to app
    db.app = app
    db.init_app(app)


def example_data():
    """Example data for test database"""

    # USERS

    u1 = User(name='John Doe', email='jd@gmail.com', password='jd123')
    u2 = User(name='Chase Bunny', email='cb@gmail.com', password='cb123')
    u3 = User(name='Phoebe Buffet', email='pb@gmail.com', password='pb123')

    db.session.add_all([u1, u2, u3])
    db.session.commit()

    # FOODS
    f1 = Food(food='tomato', quantity='2', added_on='2018-05-07')
    f2 = Food(food='salmon', quantity='1', added_on='2018-05-07')
    f3 = Food(food='lemon', quantity='3', added_on='2018-05-07')
    
    db.session.add_all([f1, f2, f3])
    db.session.commit()

    # REFRIGERATORS
    r1 = Refrigerator(user_id='1', food_id='1')
    r2 = Refrigerator(user_id='1', food_id='2')
    r3 = Refrigerator(user_id='2', food_id='3')
    
    db.session.add_all([r1, r2, r3])
    db.session.commit()

    print "ADDED TO DB"


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."

# db.create_all()
