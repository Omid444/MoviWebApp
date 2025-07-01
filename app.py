from flask import Flask, request
from models import db, User, Movie
from data_manager import DataManager
from omdb_movie_fetcher import fetch_data
import os



app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "data", "users_favorite_movies.db")

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

data_manager = DataManager()



@app.route('/')
def home():
    """The home page of your application.
    Show a list of all registered users and a form for adding new users"""
    users = data_manager.get_users()
    return str(users)


@app.route('/users', methods=['POST'])
def add_user():
    """When the user submits the “add user” form, a POST request is made.
    The server receives the new user info,
    adds it to the database, then redirects back to /"""
    name = request.form.get('name')
    data_manager.create_user(name)


@app.route('/users/<int:user_id>/movies', methods=['GET'])
def display_user_movies(user_id):
    """When you click on a username,
    the app retrieves that user’s list of favorite movies and displays it"""
    user_movies = Movie.query.join(User).filter(User.id == user_id)


@app.route('/users/<int:user_id>/movies', methods=['POST'])
def add_movie(user_id):
    """Add a new movie to a user’s list of favorite movies"""
    movie_title = request.form.get('title')
    new_movie = fetch_data(movie_title)
    data_manager.add_movie(new_movie)


@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_movie(user_id, movie_id):
    """Update the details of a specific movie in a user’s list"""
    #user = User.query.filter(User.id == user_id).first()
    new_title = request.form.get('title')
    data_manager.update_movie(movie_id=movie_id, new_title=new_title)


@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def delete_movie(user_id, movie_id):
    """Remove a specific movie from a user’s favorite movie list"""
    data_manager.delete_movie(movie_id)


if __name__ == '__main__':
    with app.app_context():
       db.create_all()

    app.run(host='0.0.0.0', port=5000)
