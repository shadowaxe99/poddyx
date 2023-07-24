# backend/models.py

from flask_sqlalchemy import SQLAlchemy


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)
  roles = db.Column(db.String(60))

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(180), nullable=False)
  content = db.Column(db.Text)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))