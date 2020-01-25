from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    zipcode = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self): 
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "zipcode": self.zipcode,
            "id": self.id
        }

class Lawyer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    zipcode = db.Column(db.String(120), unique=False, nullable=False)
    lawfirm = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self): 
        return '<Lawyer %r>' % self.name

    def serialize(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "zipcode": self.zipcode,
            "id": self.id,
            "lawfirm": self.lawfirm

        }