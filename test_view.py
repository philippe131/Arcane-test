from flask import Flask
from flask_testing import TestCase
from app import app
from models import db
import unittest, os

class TestViews(TestCase):

    # Config the app and database
    def create_app(self):
        app.config['TESTING'] = True
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'dbTest.sqlite')
        db.init_app(app)
        return app

    # Check for response 200 for GET /users/<id>
    def test_get_user(self):
        tester = app.test_client(self)
        response = tester.get("/users/1")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check for response 200 for GET /users
    def test_get_users(self):
        tester = app.test_client(self)
        response = tester.get("/users")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Create the db before every test
    def setUp(self):
        db.create_all()

    # Delete the db after every test
    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()
