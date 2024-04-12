#!/usr/bin/env python3

from random import choice as rc

from faker import Faker #type:ignore

from app import app
from models import db, Movie

fake = Faker()

def seed_database():
    # Set up the Flask application context
    with app.app_context():
        # Delete all existing movies
        Movie.query.delete()

        # Generate and save 50 movies
        for _ in range(50):
            movie = Movie(
                title=fake.sentence(nb_words=4),
                release_date=fake.date_this_year(),
                runtime=fake.random_int(min=60, max=180),
                director=fake.name(),
                cast=', '.join(fake.name() for _ in range(fake.random_int(min=1, max=5))),
            )
            db.session.add(movie)

        # Commit the changes to the database
        db.session.commit()

        print("Database seeded with 50 movies.")

if __name__ == '__main__':
    seed_database()