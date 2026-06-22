from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

class Credential(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    website = db.Column(
        db.String(255),
        nullable=False
    )

    username = db.Column(
        db.String(255),
        nullable=False
    )

    encrypted_password = db.Column(
        db.Text,
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id")
    )