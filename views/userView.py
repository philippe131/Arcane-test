from flask import Blueprint, request, jsonify
from views import app
from createBd import db
from models import userModel
from schemas import userSchema
import datetime

# create the user Blueprint
users = Blueprint('users', __name__)

@users.route('/users', methods=['GET'])
def users_index():
    return 'Blueprint users!'

# Create a user
@users.route('/users', methods=['POST'])
def add_user():

    last_name = request.json['last_name']
    first_name = request.json['first_name']
    date_birth = request.json['date_birth']

    # Create a date object and an object User with the fetched data
    date_birth_obj = datetime.datetime.strptime(date_birth, '%d/%m/%Y')
    new_user = userModel.User(last_name, first_name, date_birth_obj)

    # Add the new object to the bdd
    db.session.add(new_user)
    db.session.commit()

    # What we return to the client
    return userSchema.user_schema.jsonify(new_user)

# Register blueprint
app.register_blueprint(users)
