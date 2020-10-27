from flask import Flask, request
from flask_testing import TestCase
from app import app
from models import db
import unittest, os

class TestViews(TestCase):

    # Test data user
    last_name = "Gnansounou"
    first_name = "Philippe"
    date_birth = "20/04/1998"

    # Test data property
    name = "property 1"
    description = "description property 1"
    type = "First type"
    city = "Oslo"
    nb_pieces = 2
    feature_pieces = "Big"
    Owner = "Gnansounou"

    # Config the app and database
    def create_app(self):
        app.config["TESTING"] = True
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "dbTest.sqlite")
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

    # Check for response 200 for POST /users
    def test_create_user(self):

        # Pass the test data to POST /users
        tester = app.test_client(self)
        response = tester.post(
        "/users", json = { "last_name": self.last_name,
        "first_name": self.first_name, "date_birth": self.date_birth})
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check for response 200 for PUT /users/<id>
    def test_update_user(self):

        # Post the test data
        tester = app.test_client(self)
        tester.post("/users", json = { "last_name": self.last_name,
        "first_name": self.first_name, "date_birth": self.date_birth})

        # Update by swaping last_name and first_name
        response = tester.put("/users/1", json = { "last_name": self.first_name,
        "first_name": self.last_name, "date_birth": self.date_birth})

        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check for response 200 for GET /property/<id>
    def test_get_property(self):
        tester = app.test_client(self)
        response = tester.get("/properties/1")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check for response 200 for GET /properties
    def test_get_properties(self):
        tester = app.test_client(self)
        response = tester.get("/properties")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check for response 200 for POST /property
    def test_create_property(self):

        # Add a client because we can't add a property without a client to fill property.owner
        tester = app.test_client(self)
        tester.post("/users", json = { "last_name": self.last_name,
        "first_name": self.first_name, "date_birth": self.date_birth})

        # Add a property with property.owner = user.last_name
        response = tester.post("/properties", json
        = { "name": self.name, "description": self.description, "type": self.type,
        "city": self.city, "nb_pieces": self.nb_pieces,
        "feature_pieces": self.feature_pieces, "owner": self.last_name})

        # Check the code response
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check for response 200 for PUT /property/<id>
    def test_update_property(self):

        # Add a client because we can't add a property without a client to fill property.owner
        tester = app.test_client(self)
        tester.post("/users", json = { "last_name": self.last_name,
        "first_name": self.first_name, "date_birth": self.date_birth})

        # Add a property with property.owner = user.last_name
        tester.post("/properties", json= { "name": self.name,"description": self.description,
         "type": self.type, "city": self.city, "nb_pieces": self.nb_pieces,
        "feature_pieces": self.feature_pieces, "owner": self.last_name})

        # Update property by adding "update" to the name
        response = tester.put("/properties/1", json= { "name": self.name + "update","description": self.description,
         "type": self.type, "city": self.city, "nb_pieces": self.nb_pieces,
        "feature_pieces": self.feature_pieces, "owner": self.last_name})

        # Check the code response
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Create the db before every test
    def setUp(self):
        db.create_all()

    # Delete the db after every test
    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == "__main__":
    unittest.main()
