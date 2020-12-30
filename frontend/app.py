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
import mimetypes


app = Flask(__name__, static_url_path='/static')
moment = Moment(app)
app.config.from_object('config')
#db = SQLAlchemy(app)
#migrate=Migrate (app,db)





@app.route('/', methods=['GET'])
def home():
	return render_template('index.html')

@app.route('/add-product', methods=['GET'])
def add_product():
	return render_template('add_product.html')

@app.route('/cart', methods=['GET'])
def cart():
	return render_template('cart.html')

@app.route('/edit-product', methods=['GET'])
def edit_product():
	return render_template('edit_product.html')

@app.route('/login', methods=['GET'])
def login():
	return render_template('login.html')

@app.route('/manage-products', methods=['GET'])
def manage_products():
	return render_template('manage_products.html')

@app.route('/product', methods=['GET'])
def product():
	return render_template('product.html')

@app.route('/signup', methods=['GET'])
def signup():
	return render_template('signup.html')










@app.template_global()
def static_include(filename):
    fullpath = os.path.join(app.static_folder, filename)
    with open(fullpath, 'r') as f:
        return f.read()



"""


<script type="text/javascript">
  {{static_include("js/jquery.js") | safe}}
</script>
<script type="text/javascript">
  {{static_include("js/bootstrap.bundle.min.js")| safe}}
</script>
<script type="text/javascript">
  {{static_include("js/bootstrap.min.js")| safe}}
</script>
<link rel="stylesheet" href="static/css/bootstrap.min.css">


"""













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