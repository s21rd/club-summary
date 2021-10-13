import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pyodbc

load_dotenv()

# flask setting
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]


# database setting
DB_USER = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_DATABASE = os.environ["DB_DATABASE"]
DB_PORT = os.environ["DB_PORT"]

params = quote_plus(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=tcp:{DB_HOST},{DB_PORT};DATABASE={DB_DATABASE};UID={DB_USER};PWD={DB_PASSWORD};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"mysql+pyodbc:///?odbc_connect={params}?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

import web.views
