from models import db, User, Movie


class DataManager():
    # Define Crud operations as methods
    def create_user(self, name):
        """Add a new user to your database"""
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

    def get_users(self):
        """Return a list of all users in your database"""
        return User.query.all()

    def get_movies(self, user_id):
        """Return a list of all movies of a specific user"""
        return Movie.query.join(User).filter(User.id == user_id).all()

    def add_movie(self, movie):
        """Add a new movie to a user’s favorites"""
        db.session.add(movie)
        db.session.commit()

    def update_movie(self, movie_id, user_id, new_title):
        """Update the details of a specific movie in the database"""
        movie_to_update = Movie.query.filter(Movie.id == movie_id, user_id == user_id).first()
        movie_to_update.title = new_title
        db.session.commit()

    def delete_movie(self, user_id, movie_id):
        """Delete the movie from the user’s list of favorites"""
        movie_to_delete = Movie.query.filter(movie_id == movie_id and user_id==user_id).first()
        print(movie_to_delete)
        if movie_to_delete:
            db.session.delete(movie_to_delete)
            db.session.commit()
