from flask import Blueprint, request, jsonify
from views import app, db
from models import propertyModel
from schemas import propertySchema

# create the propreties Blueprint
properties = Blueprint('properties', __name__)

@properties.route('/properties')
def property_index():
    return 'Blueprint properties!'

# Register blueprint
app.register_blueprint(properties)
