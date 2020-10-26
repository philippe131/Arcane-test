from models import db, app, userModel, propertyModel
from schemas import userSchema, propertySchema
import os

# Init bdd
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

# Create the database
if __name__ == "__main__":
    db.create_all()
