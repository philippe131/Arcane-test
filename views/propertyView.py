from flask import Blueprint, request, jsonify
from views import app, db
from models import propertyModel
from schemas import propertySchema

# create the propreties Blueprint
properties = Blueprint('properties', __name__)

# Get single property
@app.route('/properties/<id>', methods=['GET'])
def get_property(id):
    # product have meth query because it is a db model
    property = propertyModel.Property.query.get(id)
    return propertySchema.property_schema.jsonify(property)

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
    city = request.json['city']
    nb_pieces = request.json['nb_pieces']
    feature_pieces = request.json['feature_pieces']
    owner = request.json['owner']

    # Create an object property with the fetched data
    new_property = propertyModel.Property(name, description, type, city, nb_pieces, feature_pieces, owner)

    # Add the new object to the bdd
    db.session.add(new_property)
    db.session.commit()

    # What we return to the client
    return propertySchema.property_schema.jsonify(new_property)

# Update a property
@properties.route('/properties/<id>', methods=['PUT'])
def update_property(id):

    property = propertyModel.Property.query.get(id)

    # recover each json field
    name = request.json['name']
    city = request.json['city']
    description = request.json['description']
    nb_pieces = request.json['nb_pieces']
    feature_pieces = request.json['feature_pieces']
    type = request.json['type']
    owner = request.json['owner']

    # fill object Product with the fetched data
    property.name = name
    property.city = city
    property.description = description
    property.nb_pieces = nb_pieces
    property.feature_pieces = feature_pieces
    property.type = type
    property.owner = owner

    # Commit the change
    db.session.commit()

    # What we return to the client
    return propertySchema.property_schema.jsonify(property)



# Register blueprint
app.register_blueprint(properties)
