from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets
import os
from models import db
from models import (NotReceived, User, Product, Order, 
	Image, db_drop_and_create_all, populate_tables) 
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

	# create and configure the app
	SECRET
	app = Flask(__name__)
	#db=SQLAlchemy(app)
	if testing:
		app.config.from_object(config_test)
	else:
		app.config.from_object(config)
	#print(DOCKER)
	if DOCKER:
		app.config["SQLALCHEMY_DATABASE_URI"]=(
		"sqlite:////database//database.sqlite")
	#print(SECRET, flush=True)
	db.app = app
	migrate = Migrate(app,db)
	db.init_app(app)
	try:
		db.create_all()
	except:
		pass


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
