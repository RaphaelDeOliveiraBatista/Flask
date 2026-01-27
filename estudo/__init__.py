from flask import Flask
from sqlalchemy import sqlalchemy
from flask_migrate import flask_migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = sqlalchemy(app)
migrate = migrate(app,db)

from estudo.views import homepage
from estudo.models import Contato