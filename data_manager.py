from models import db, User, Movie

class DataManager():
  # Define Crud operations as methods
    def create_user(self, name):
      new_user = User(name=name)
      db.session.add(new_user)
      db.session.commit()


    def get_users(self):
        return User.query.all()


    def get_movies(self, user_id):
        return User.query.filter(User.id == user_id)


    def add_movie(self, movie):
        new_movie = Movie()
