"""Tests for Foodio"""

import unittest

from server import app
from model import db, connect_to_db

class FoodioTestsDatabase(unittest.TestCase):
    """Flask test that uses the database"""

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

    def tearDown(self):
        """Do at the end of every test"""

        db.session.close()
        db.drop_all()

    def test_users(self):
        """Test that user information displays on page"""

        result = self.client.get('/test')
        self.assertIn('Chase Bunny', result.data)
