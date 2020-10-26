from models import app, db

# User Class/Model
class User(db.Model):
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80), primary_key=True)
    date_birth = db.Column(db.Date)

    def __init__(self, first_name, last_name, date_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_birth = date_birth
