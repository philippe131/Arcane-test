from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Init app
app = Flask(__name__)

# Init bdd
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '../db.sqlite')
db = SQLAlchemy(app)

from views import propertyView
from views import userView
