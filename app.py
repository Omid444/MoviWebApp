from flask import Flask
from models import db, User, Movie
import os


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "data", "library.sqlite")

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db.init_app(app)


with app.app_context():
   db.create_all()












if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
