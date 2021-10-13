import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

# flask setting
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]


# database setting
DB_USER = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_DATABASE = os.environ["DB_DATABASE"]

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

import web.views
