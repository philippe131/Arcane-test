# Arcane-test

This project is the result of the Arcane technical test

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
pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy
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

To check the fields of the created, go at the end of the Readme

Create a new user, for the date_birth use the format : Day/Month/year
```
Post request to http://127.0.0.1:5000/users with a json containing the fields of an user.
```

## Database description

user (last_name = String, first_name = String, date_birth = Date). For the
