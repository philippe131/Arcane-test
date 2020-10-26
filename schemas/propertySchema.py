from schemas import ma

# property Schema
class PropertySchema(ma.Schema):
    class Meta:
        fields = ('name', 'description', 'type', 'city', 'pieces', 'feature_pieces', 'owner')

# Init property schema
property_schema = PropertySchema()
properties_schema = PropertySchema(many=True)
