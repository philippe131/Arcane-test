from flask import Blueprint, request, jsonify
from views import app, db
from models import propertyModel
from schemas import propertySchema

# create the propreties Blueprint
properties = Blueprint('properties', __name__)

# Get all property
@properties.route('/properties', methods=['GET'])
def get_properties():
    # property have meth query because it is a db model
    all_properties = propertyModel.Property.query.all()
    result = propertySchema.properties_schema.dump(all_properties)
    return jsonify(result)

# Create a property
@properties.route('/properties', methods=['POST'])
def add_property():

    name = request.json['name']
    description = request.json['description']
    type = request.json['type']
    ville = request.json['ville']
    nb_piece = request.json['nb_piece']
    carac_piece = request.json['carac_piece']
    owner = request.json['owner']

    # Create an object property with the fetched data
    new_property = propertyModel.Property(name, description, type, ville, nb_piece, carac_piece, owner)

    # Add the new object to the bdd
    db.session.add(new_property)
    db.session.commit()

    # What we return to the client
    return propertySchema.property_schema.jsonify(new_property)


# Register blueprint
app.register_blueprint(properties)
