from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, INTEGER, String, text, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()



class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.INTEGER, primary_key= True,autoincrement=True)
    name = db.Column(db.String, nullable=False)


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    director = db.Column(db.String, nullable=False)
    year = db.Column(db.String, nullable=False)
    poster_url = db.Column(db.String, nullable=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey("user.id") , nullable=False)
    #user = relationship('User', back_populates='')


