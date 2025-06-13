from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(10), nullable=False) 

class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pickup = db.Column(db.String(100))
    destination = db.Column(db.String(100))
    status = db.Column(db.String(100), default='Pending') 
    passenger_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    driver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
