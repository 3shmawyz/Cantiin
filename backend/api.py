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
		body = request.get_json()
		try:
			name = body.get("name",None)
			price = body.get("price",None)
			in_stock = body.get("in_stock",None)
			seller = body.get("seller",None)
		except:
			return my_error(status=400, 
				description = "there is no request body")


		name_validation = validate_must(
			input=name,type="s",input_name_string="name")




		#Now we will validate the in_stock input
		if in_stock_validation["case"] == True:
			# Success: True or false
			in_stock=in_stock_validation["result"]		
		else:
			# Failure: Can't convert to boolean or None (Impossible)
			return in_stock_validation["result"]















		all_products=Product.query


		name_validation = validate_string(name,"name")
		#Now we will validate the new name of product
		if name_validation["case"] == 1:
			# Success: string
			name=name_validation["result"]
		elif name_validation["case"] == 2:
			# Failure: Can't convert to string
			return my_error(status=name_validation["result"]["status"],
				description=name_validation["result"]["description"])
		else:
			# no Input is given, result = None
			return my_error(status=400,description=
				"product name is missing")


		price_validation = validate_float(price,"price")
		#Now we will validate the new name of product
		if price_validation["case"] == 1:
			# Success: string
			name=name_validation["result"]
		elif name_validation["case"] == 2:
			# Failure: Can't convert to string
			return my_error(status=name_validation["result"]["status"],
				description=name_validation["result"]["description"])
		else:
			# no Input is given, result = None
			return my_error(status=400,description=
				"product name is missing")





		


		name_validation = validate_product_name(name)
		if name_validation[0]==True:
			name = name_validation[1]
			#This is the valid data
		else:
			return name_validation[1]
			#This is the error message




		price_validation = validate_recipe(price)
		if price_validation[0]==True:
			price = price_validation[1]
			#This is the valid data
		else:
			return price_validation[1]
			#This is the error message

		all_drinks = Drink.query

		any_drink = all_drinks.filter(Drink.title.ilike(title)).all()
		if len(any_drink)!=0:
			return my_error(status = 422, 
				description="there is already a drink with this name")



		drink = Drink(title = title.strip(), recipe = str(recipe))
		drink.insert()
		return jsonify({
			"success":True,"drinks":[drink.long()]
			}),200

		












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



	





	@app.errorhandler(404)
	def not_found(error):
		return jsonify({"success":False,"error":404,
			"message":"resource not found"}),404

	@app.errorhandler(422)
	def unprocessible(error):
		return jsonify({"success":False,"error":422,
			"message":"unprocessible"}),422


	@app.errorhandler(400)
	def bad_request(error):
		return jsonify({"success":False,"error":400,
			"message":"bad request"}),400


	@app.errorhandler(405)
	def method_not_allowed(error):
		return jsonify({"success":False,"error":405,
			"message":"method not allowed"}),405
	
	return app	

if __name__ == '__main__':
		create_app().run()	