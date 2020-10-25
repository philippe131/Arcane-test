from app import db, ma

# User Class/Model
class User(db.Model):
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80), primary_key=True)
    date_birth = db.Column(db.Date)

    def __init__(self, first_name, last_name, date_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_birth = date_birth

#  User schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('first_name', 'last_name', 'date_birth')

# Init UserSchema
user_schema = UserSchema()
users_schema = UserSchema(many=True)


# property Class/Model
class Property(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(250))
    type = db.Column(db.String(50))
    city = db.Column(db.String(80))
    pieces = db.Column(db.Integer)
    feature_pieces = db.Column(db.String(300))
    owner = db.Column(db.Date, db.ForeignKey('user.last_name'), nullable=False)

    def __init__(self, name, description, type, city, pieces, feature_pieces, owner):
        self.name = name
        self.description = description
        self.type = type
        self.city = city
        self.pieces = pieces
        self.feature_pieces = feature_pieces
        self.owner = owner

# property Schema
class PropertySchema(ma.Schema):
    class Meta:
        fields = ('name', 'description', 'type', 'city', 'pieces', 'feature_pieces', 'owner')

# Init property schema
property_schema = PropertySchema()
properties_schema = PropertySchema(many=True)

# Create the database
if __name__ == "__main__":
    db.create_all()
