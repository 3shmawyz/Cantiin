import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy
from random import shuffle
import json
from models import (db, Product, Order)
from random import shuffle
from functions import *
"""
endpoints:
	1)	"/clear_tables"-------->"GET" , "OPTIONS"
	2)	"/populate" ->--------->"GET" , "OPTIONS"
	3)	"/products"	->--------->"GET" , "OPTIONS"

"""





def create_app(test_config=None,testing=False):
	# create and configure the app
	app = Flask(__name__)
	#db=SQLAlchemy(app)
	if testing:
		app.config.from_object("config_test")
	else:
		app.config.from_object("config")
	db.app = app
	migrate = Migrate(app,db)
	db.init_app(app)
	#populate_tables()
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
		




	"""
	1)	"/clear_tables"-------->"GET" , "OPTIONS"
	"""
	@app.route("/clear_tables", methods=["GET"])
	def clear_all_tables():
		db_drop_and_create_all()
		"""
Tests: test_02_populate_test
		"""
		return jsonify({"success":True})








	"""
	2)	"/populate" ->--------->"GET" , "OPTIONS"
	"""
	@app.route("/populate", methods=["GET"])
	def populate_all_tables():
		#This endpoint will clear all the data in the database and 
		#populate with new data
		try:
			populate_tables()
			return jsonify({"success":True})
		except:
			abort(422) #Unprocessible
		"""
Tests: test_01_clear_tables
		"""
		


	"""
	3)	"/products"	->--------->"GET" , "OPTIONS"
	"""
	@app.route("/products", methods=["GET"])
	def get_products():
	#This endpoint will return all the products		
		#recievng inputs:
		#in_stock has a fall back value of True (The default)
		in_stock = request.args.get('in_stock',True)


		#in stock now has one of two values
		#1) input value
		#2) True (Fall back value)
		#-	I can not be equal to None at all
		#-	Even if equal to None, it will be rejected
		in_stock_validation = validate_must(
			input=in_stock,type="b",input_name_string="in_stock")

		#Now we will validate the in_stock input
		if in_stock_validation["case"] == True:
			# Success: True or false
			in_stock=in_stock_validation["result"]		
		else:
			# Failure: Can't convert to boolean or None (Impossible)
			return in_stock_validation["result"]

		#Now: There are 2 possibilties
			#1) in_stock = True
			#2) in_stock=False
			#input now must have been converted to True or False

		if in_stock == True:
			products = get_in_stock_products()
		else:
			products = Product.query.order_by(Product.id).all()
		
		to_return=[p.simple() for p in products]
		return jsonify({"success":True,"products":to_return})
		






	@app.route("/products", methods=["POST"])
	def post_products():
	#This endpoint will add a new product
		try:
			body = request.get_json()
		except:
			return my_error(status=400,
				description="request body can not be parsed to json")
		try:
			name = body.get("name",None)
			price = body.get("price",None)
			in_stock = body.get("in_stock",None)
			seller_id = body.get("seller_id",None)
		except:
			return my_error(status=400, 
				description = "there is no request body")


		#Validating inputs one by one
		name_validation = validate_must(
			input=name,type="s",input_name_string="name",
			minimum=3,maximum=150)
		price_validation = validate_must(
			input=price,type="f",input_name_string="price",
			minimum=0.1,maximum=1000000)
		in_stock_validation = validate_must(
			input=in_stock,type="b",input_name_string="in_stock")
		seller_id_validation = validate_must(
			input=seller_id,type="i",input_name_string="seller_id",
			minimum=1,maximum=100000000000000000)

		#Validating inputs a group
		val_group=validate_must_group(
			[name_validation,price_validation,
			in_stock_validation,seller_id_validation])

		#Now we will validate all inputs as a group
		if val_group["case"] == True:
			# Success: they pass the conditions
			name,price,in_stock,seller_id=val_group["result"]		
		else:
			# Failure: Something went wrong
			return val_group["result"]

		#Create the product
		new_product = Product(name=name, price=price,
			seller_id=seller_id, in_stock=in_stock)

		#Insert the product in the database
		try:
			new_product.insert()
			return jsonify(
				{"success":True,"product":new_product.simple()})
		except Exception as e:
			abort(500)


		


	@app.route("/products/<int:product_id>", methods=["PUT"])
	def edit_products(product_id):
	#This endpoint will add a new product
		try:
			body = request.get_json()
		except:
			return my_error(status=400,
				description="request body can not be parsed to json")
		try:
			name = body.get("name",None)
			price = body.get("price",None)
			in_stock = body.get("in_stock",None)
		except:
			return my_error(status=400, 
				description = "there is no request body")
		
		#There can not be 0 fields to change
		#There must be at least one input field
		if (name==None and price==None and in_stock==None):
			return my_error(status=400, 
				description = "you must at least enter"
				" one field to change")

		products_query=Product.query

		product_id_validation=validate_model_id(
			input_id=product_id,model_query=products_query
			,model_name_string="product")
		if product_id_validation["case"]==1:
			#The product exists
			product=product_id_validation["result"]

		else:
			#No product with this id, can not convert to int,
			# or id is missing (Impossible)
			return my_error(
				status=product_id_validation["result"]["status"],
				description=product_id_validation
				["result"]["description"])
		 
		#Now, we have "product", this is essential

		#there will be no None
		if name == None:name=product.name
		if price == None:price=product.price
		if in_stock == None:in_stock=product.in_stock
		#Now there is no None
		#There are default values
		#This step can not change it's place because
		#here we need default values
		
		name_validation = validate_must(
			input=name,type="s",input_name_string="name",
			minimum=3,maximum=150)
		price_validation = validate_must(
			input=price,type="f",input_name_string="price",
			minimum=0.1,maximum=1000000)
		in_stock_validation = validate_must(
			input=in_stock,type="b",input_name_string="in_stock")
		#seller_id_validation = validate_must(
		#	input=seller_id,type="i",input_name_string="seller_id",
		#	minimum=1,maximum=100000000000000000)
		#seller_id can not change


		val_group=validate_must_group(
			[name_validation,price_validation,
			in_stock_validation])

		#Now we will validate all inputs as a group
		if val_group["case"] == True:
			# Success: they pass the conditions
			name,price,in_stock,=val_group["result"]		
		else:
			# Failure: Something went wrong
			return val_group["result"]

		try:
			product.update()
			return jsonify(
				{"success":True,"product":product.simple()})
		except Exception as e:
			abort(500)


		












	def return_error(id):
		if id==1:
			return jsonify({"success":False,"error":400,
			"message":"bad request",
			"details":"missing request body"
			}),400
		if id==2:
			return jsonify({"success":False,"error":400,
			"message":"bad request",
			"details":"missing required variables in request body"
			}),400
		if id==3:
			return jsonify({"success":False,"error":422,
			"message":"unprocessible",
			"details":"there is a mistake in data types"
			}),422
		if id==4:
			return jsonify({"success":False,"error":422,
			"message":"unprocessible",
			"details":"this category id is not in the database"
			}),422			

		if id==5:
			return jsonify({"success":False,"error":422,
			"message":"unprocessible",
			"details":"this question id is not in the database"
			}),422			



	




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


	
	return app	

if __name__ == '__main__':
		create_app().run()	