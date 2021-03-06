from models import db

# property Class/Model
class Property(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(250))
    type = db.Column(db.String(50))
    city = db.Column(db.String(80))
    nb_pieces = db.Column(db.Integer)
    feature_pieces = db.Column(db.String(300))
    owner = db.Column(db.String(80), db.ForeignKey('user.last_name'), nullable=False)

    def __init__(self, name, description, type, city, nb_pieces, feature_pieces, owner):
        self.name = name
        self.description = description
        self.type = type
        self.city = city
        self.nb_pieces = nb_pieces
        self.feature_pieces = feature_pieces
        self.owner = owner
