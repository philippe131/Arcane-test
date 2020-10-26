from models import app, db

# User Class/Model for the database
class User(db.Model):

    # All the column of the table
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    date_birth = db.Column(db.Date)

    def __init__(self, first_name, last_name, date_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_birth = date_birth
