from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets
import os
from models import db
from models import (NotReceived, User, Product, Order, 
	Image, db_drop_and_create_all, populate_tables) 



class config:
	#SECRET_KEY=os.urandom(32)
	SECRET_KEY=secrets.token_urlsafe(5000)
	basedir = os.path.abspath(os.path.dirname(__file__))
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = "sqlite:///databases/database.sqlite"
	SQLALCHEMY_TRACK_MODIFICATIONS= False

def create_app():


	app = Flask(__name__)

	app.config.from_object(config)

	SECRET_KEY=secrets.token_urlsafe(5000)
	basedir = os.path.abspath(os.path.dirname(__file__))
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS= False



	#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/test.sqlite'
	db.app = app

	db.init_app(app)
	#with app.app_context():
	#    db.create_all()
	db.create_all()
	#return app
