
from flask import Flask
import flask
app=Flask(__name__)
from . import main

from flaskr import db
db.create_books_table()


def create_app():
    
    app = Flask(__name__)
    app.register_blueprint(flask.main)
    # ... その他の設定 ...
    return app

