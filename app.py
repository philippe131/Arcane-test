from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from views.views import main
from extensions import db, ma
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

# Init db
db.init_app(app)

# Init Marshmallow
ma.init_app(app)

# Register blueprint
app.register_blueprint(main)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
