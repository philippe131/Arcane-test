# Arcane-test

This project is the result of the Arcane technical test

## Dependencies

- flask : Python server of choice.
- flask-marshmallow : Used to serialize object.
- flask-sqlalchemy : The database.
- marshmallow-sqlalchemy : Used to make the link between marshmallow and sqlalchemy.
- flasgger : Used to generate the documentation
- apispec : Required for the integration between marshmallow and flasgger


## Set up

Install pipenv
```
pip3 install pipenv
```

Install the Dependencies
```
pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy flasgger apispec
```

## Running the app

To run the app, first run the models.py file directly to create the database tables, you only need to do it once unless you change your model definitions
```
python models.py
```

Run the app itself
```
python app.py
```
