#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
import traceback
import json
import dateutil.parser
import babel
import sys,os
import logging
import datetime
from flask import (Flask, 
	render_template, request, Response, flash, 
	redirect, url_for,abort, jsonify)
from flask_migrate import Migrate
from flask_moment import Moment
#from flask_sqlalchemy import SQLAlchemy
#from flask_wtf import Form
from logging import Formatter, FileHandler
#from sqlalchemy import func
#from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField,BooleanField,RadioField
#from wtforms.validators import DataRequired, AnyOf, URL



app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
#db = SQLAlchemy(app)
#migrate=Migrate (app,db)






@app.route('/', methods=['GET'])
def home():
	return render_template('home.html')






























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







if __name__=="__main__":
	app.run(port=8000)