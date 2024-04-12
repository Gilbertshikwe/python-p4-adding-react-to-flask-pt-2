from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Movie(db.Model, SerializerMixin):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.Date)
    runtime = db.Column(db.Integer)
    director = db.Column(db.String)
    cast = db.Column(db.String)

    def __repr__(self):
        return f'<Movie {self.title}>'