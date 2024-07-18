from models import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column("id",  db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(1024), nullable=False) 

    reads = db.relationship("Read", backref="users", lazy=True)
    employees = db.relationship("Employee", backref="users", lazy=True)