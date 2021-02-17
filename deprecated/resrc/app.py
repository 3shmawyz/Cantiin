TESTING=True
"""
TESTING=False 	IN CASE OF PRODUCTION
TESTING=True 	IN CASE OF TESTING
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets
import os
from __init__ import db, SECRET
from models import (NotReceived, User, Product, Order, #Image,
	db_drop_and_create_all, populate_tables)
from flask_cors import CORS
from flask_pydantic import validate


if "SECRET" in os.environ:
	SECRET = os.environ["SECRET"]




class config:
	#SECRET_KEY=os.urandom(32)
	SECRET_KEY=secrets.token_urlsafe(5000)
	basedir = os.path.abspath(os.path.dirname(__file__))
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = "sqlite:///databases/database.sqlite"
	SQLALCHEMY_TRACK_MODIFICATIONS= False


class config_test:
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = "sqlite:///databases/test.sqlite"

class config_docker:
	SQLALCHEMY_DATABASE_URI = "sqlite:////database//database.sqlite"


def create_app(DOCKER=False,testing=TESTING):
	app = Flask(__name__)
	app.config.from_object(config)
	if TESTING:
		app.config.from_object(config_test)
	if DOCKER:
		app.config.from_object(config_docker)

	db.app = app
	db.init_app(app)
	db.create_all()

	CORS(app,resources={r"*":{"origins":"*"}})
	@app.after_request
	def after_request(response):
		response.headers.add("Access-Control-allow-Origin","*")
		response.headers.add("Access-Control-allow-Headers",
			"Content-Type,Autorization,true")
		response.headers.add("Access-Control-allow-Methods",
			"GET,PUT,POST,DELETE,OPTIONS")
		db.session.rollback()
		return response












































































	@app.errorhandler(400)
	def bad_request(error):
		return jsonify({"success":False,"error":400,
			"message":"bad request"}),400


	@app.errorhandler(401)
	def unauthorized(error):
		return jsonify({"success":False,"error":401,
			"message":"unauthorized"}),401


	@app.errorhandler(403)
	def forbidden(error):
		return jsonify({"success":False,"error":403,
			"message":"forbidden"}),403


	@app.errorhandler(404)
	def not_found(error):
		return jsonify({"success":False,"error":404,
			"message":"not found"}),404


	@app.errorhandler(405)
	def method_not_allowed(error):
		return jsonify({"success":False,"error":405,
			"message":"method not allowed"}),405


	@app.errorhandler(422)
	def unprocessible(error):
		return jsonify({"success":False,"error":422,
			"message":"unprocessible"}),422


	@app.errorhandler(500)
	def internal_server_error(error):
		return jsonify({"success":False,"error":500,
			"message":"internal server error"}),500



	def test_only():
		if testing == False:
			abort(404)


	return app

if __name__ == '__main__':
	create_app().run()
