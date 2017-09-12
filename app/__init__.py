from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstraps import Bootstrap
from app import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
from app import views

