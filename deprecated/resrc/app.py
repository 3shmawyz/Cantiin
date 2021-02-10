from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets
import os
from models import db
from models import (NotReceived, User, Product, Order, #Image, 
	db_drop_and_create_all, populate_tables) 
from flask_cors import CORS


class config:
	#SECRET_KEY=os.urandom(32)
	SECRET_KEY=secrets.token_urlsafe(5000)
	basedir = os.path.abspath(os.path.dirname(__file__))
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = "sqlite:///databases/database.sqlite"
	SQLALCHEMY_TRACK_MODIFICATIONS= False


class config_test:
	#SECRET_KEY=os.urandom(32)
	SECRET_KEY=secrets.token_urlsafe(5000)
	basedir = os.path.abspath(os.path.dirname(__file__))
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = "sqlite:///databases/test.sqlite"
	SQLALCHEMY_TRACK_MODIFICATIONS= False


def create_app():

	app = Flask(__name__)

	app.config.from_object(config)


	#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/test.sqlite'
	db.app = app

	db.init_app(app)
	#with app.app_context():
	#    db.create_all()
	db.create_all()
	#return app

	CORS(app,resources={r"*":{"origins":"*"}})
	@app.after_request
	def after_request(response):
		response.headers.add("Access-Control-allow-Origin","*")
		response.headers.add("Access-Control-allow-Headers",
			"Content-Type,Autorization,true")
		response.headers.add("Access-Control-allow-Methods",
			"GET,PUT,POST,DELETE,OPTIONS")
		db.session.rollback()
		#print("roll back", flush=True)
		return response













































































	return app
