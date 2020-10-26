# Arcane-test

This project is the result of the Arcane technical test.

## Potential futur improvements

- Implements a test for every http request.
- Handle error raised when you try to create a property with an unknow owner.
- Allow users to only view properties from one city
- Restrict access of the users only to their propreties
- Allow users to delete their properties
- Allow users to find a properties using other filter like the number of pieces or the name of the owner


## Dependencies

- flask : Python server of choice.
- flask-marshmallow : Used to serialize object.
- flask-sqlalchemy : The database.
- marshmallow-sqlalchemy : Used to make the link between marshmallow and sqlalchemy.


## Set up

Install pipenv
```
pip3 install pipenv
```

Install the Dependencies
```
pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy Flask-Testing
```

## Running the app

To run the app, first run the createBd.py file to create the database tables, you only need to do it once unless you change your model definitions
```
python createBd.py
```

Run the app itself
```
python app.py
```

## How to use it (Once the database is created)

To check the fields and the specificities of the Db, go at the end of the Readme

Create a new user, for the date_birth use the format : Day/Month/year
```
POST request to http://127.0.0.1:5000/users with a json containing the fields of an user.
```

Recover all the users from the Database or just one
```
GET request to http://127.0.0.1:5000/users or GET request to http://127.0.0.1:5000/users/<id>
```

Update a user using his id
```
PUT request to http://127.0.0.1:5000/users/<id>
```

Create a new property
```
POST request to http://127.0.0.1:5000/users with a json
```

Get all the properties or just one
```
GET request to http://127.0.0.1:5000/propreties or GET request to http://127.0.0.1:5000/propreties/<id>
```

Update a property using his id
```
PUT request to http://127.0.0.1:5000/properties/<id>
```

## Database description

user (id = Integer, last_name = String, first_name = String, date_birth = Date)

property (id = Integer, name = String, description = String, type = String, city = string, nb_piece = Integer, feature_pieces = String, owner = String)

You can't insert a property without owner.
