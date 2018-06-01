"""Tests for Foodio"""

import unittest

from server import app  
from model import db, connect_to_db, example_data

class FoodioSetup(unittest.TestCase):
    """Flask test for user registration, login, logout"""

    def setUp(self):
        """initial setup"""

        # create test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # connect to test database
        connect_to_db(app, "postgresql:///testdb")

        # create tables and add sample data
        db.create_all()

        # *INSERT example data here using example_data()
        example_data()

    def tearDown(self):
        """Do at the end of every test"""

        db.session.close()
        db.drop_all()


    def test_index(self):
        """Test homepage"""
        
        client = app.test_client()
        result = client.get('/')
        self.assertIn('Email', result.data)
        print "pass index"


    def test_register_user(self):
        """Test registration - successful"""

        result = self.client.post('/registration', 
                                data={'name': 'Charlie', 
                                'email': 'charlie@gmail.com',
                                'password': 'bitme'},
                                follow_redirects=True)
        
        self.assertEqual(result.status_code, 200)
        self.assertIn('Registration successful! Please log in!', result.data)
        print "pass registration - successful"


    def test_register_user2(self):
        """Test registration - unsuccessful"""

        result = self.client.post('/registration', 
                                data={'name': 'Chase', 
                                'email': 'cb@gmail.com',
                                'password': 'cb123'}, 
                                follow_redirects=True)
        
        self.assertEqual(result.status_code, 200)
        self.assertIn('Already a member. Please log in', result.data)
        print "pass registration - unsuccessful"


    def test_login(self):
        """Test user's login - successful"""

        result = self.client.post('/login', 
                                data={'email': 'cb@gmail.com', 
                                'password': 'cb123'}, 
                                follow_redirects=True)
        
        self.assertEqual(result.status_code, 200)
        self.assertIn('Welcome, Chase Bunny!', result.data)
        print "pass login - successful"


    def test_login2(self):
        """Test user's login - unsuccessful"""

        result = self.client.post('/login', 
                                data={'email': 'dne@gmail.com', 
                                'password': 'dne123'}, 
                                follow_redirects=True)
        
        self.assertEqual(result.status_code, 200)
        self.assertIn('Invalid email or password', result.data)
        print "pass login - unsuccessful"


    def test_logout(self):
        """Test user's logout - no session"""

        result = self.client.get('/logout', 
                                follow_redirects=True)
        
        self.assertEqual(result.status_code, 200)
        self.assertIn('<b>Log In</b>', result.data)
        print "pass logout - no session"


class FoodioTestsSession(unittest.TestCase):
    """Flask test for user homepage with session"""

    def setUp(self):
        """initial setup"""

        # create test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        app.config['SECRET_KEY'] = 'drvtry1ru'
        self.client = app.test_client()

        with self.client as c:
            with c.session_transaction() as session:
                session['user'] = 2

        # connect to test database
        connect_to_db(app, "postgresql:///testdb")

        # create tables and add sample data
        db.create_all()

        # *INSERT example data here using example_data()
        example_data()

    def tearDown(self):
        """Do at the end of every test"""

        db.session.close()
        db.drop_all()

    def test_logout(self):
        """Test user's logout - session"""

        result = self.client.get('/logout',
                                follow_redirects=True)
        
        self.assertEqual(result.status_code, 200)
        self.assertIn('<b>Log In</b>', result.data)
        print "pass logout - session"


    def test_users_homepage(self):
        """Test user's homepage"""

        result = self.client.get('/user-2', 
                                follow_redirects=True)
        
        self.assertEqual(result.status_code, 200)
        self.assertIn('Food available in your refrigerator:', result.data)
        self.assertIn('Add to fridge:', result.data)
        self.assertIn('Remove from fridge:', result.data)
        self.assertIn('Recipes', result.data)
        self.assertIn('Favorite Recipes', result.data)
        print "pass users homepage"


    def test_food_data(self):
        """Test displaying food data from database"""

        result = self.client.get('/food-data.json')
        
        self.assertEqual(result.status_code, 200)
        self.assertIn('children', result.data)
        print "pass display food data"


    def test_add_food(self):
        """Test add food"""

        result = self.client.post('/add-food.json', 
                                data={'ingredient': 'cantaloupe', 
                                'quantity': '105'}, 
                                follow_redirects=True)

        self.assertEqual(result.status_code, 200)
        self.assertIn('cantaloupe', result.data)
        print "pass add food"


    def test_remove_food(self):
        """Test remove food"""

        result = self.client.post('/remove-food.json', 
                                data={'rm-ingredient': '4 tuna'}, 
                                follow_redirects=True)

        self.assertEqual(result.status_code, 200)

        #check json result for food to delete
        self.assertIn('tuna', result.data)
        print "pass remove food"


    def test_API_recipes(self):
        """Test displaying recipes via API"""

        result = self.client.get('/recipes.json')
        
        self.assertEqual(result.status_code, 200)
        self.assertIn('https://spoonacular.com/recipeImage', result.data)
        print "pass API recipe data"


    def test_add_quantity(self):
        """Test incrementing quantity by 1"""

        result = self.client.get('/add-quantity.json',
                                query_string={'food-id': '1'},
                                follow_redirects=True)

        self.assertEqual(result.status_code, 200)
        self.assertIn('3', result.data)
        print "pass add food quantity"


    def test_sub_quantity(self):
        """Test decreasing food quantity by 1"""

        result = self.client.get('/sub-quantity.json',
                                query_string={'food-id': '3'},
                                follow_redirects=True)

        self.assertEqual(result.status_code, 200)
        self.assertIn('2', result.data)
        print "pass subtract food quantity"


    def test_fav_recipes(self):
        """Test favoriting recipes - not already in favs"""

        result = self.client.get('/fav-recipes.json',
                                query_string={'title': 'Most Delicious Recipe Ever', 
                                'fav-url': 'https://recipes.com/bestEver',
                                'img': 'https://img.com/recipeImages'})
        
        self.assertEqual(result.status_code, 200)
        self.assertIn('Most Delicious Recipe Ever', result.data)
        print "pass API recipe data"


if __name__ == '__main__':
    # If called like a script, run our tests
    unittest.main()
