from flask import Blueprint, request, jsonify
from views import app
from createBd import db
from models import userModel
from schemas import userSchema
import datetime

# create the user Blueprint
users = Blueprint('users', __name__)

# Get single User
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = userModel.User.query.get(id)
    return userSchema.user_schema.jsonify(user)

# Get all user
@users.route('/users', methods=['GET'])
def get_users():
    all_users = userModel.User.query.all()
    result = userSchema.users_schema.dump(all_users)
    return jsonify(result)

# Update a user
@users.route('/users/<id>', methods=['PUT'])
def update_users(id):

    user = userModel.User.query.get(id)

    # recover each json field
    last_name = request.json['last_name']
    first_name = request.json['first_name']
    date_birth = request.json['date_birth']

    # Transform date_birth in a date object
    date_birth_obj = datetime.datetime.strptime(date_birth, '%d/%m/%Y')

    # fill object Product with the fetched data
    user.last_name = last_name
    user.first_name = first_name
    user.date_birth = date_birth_obj

    # Commit the change
    db.session.commit()

    # What we return to the client
    return userSchema.user_schema.jsonify(user)


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
