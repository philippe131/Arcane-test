from flask import Blueprint, request, jsonify
from views import app, db
from models import userModel
from schemas import userSchema

# create the user Blueprint
users = Blueprint('users', __name__)

@users.route('/users', methods=['GET'])
def users_index():
    return 'Blueprint users!'

# Register blueprint
app.register_blueprint(users)
