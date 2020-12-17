import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy
from random import shuffle
import json
from models import (db, populate_tables, get_in_stock_products,
	db_drop_and_create_all,Product, Order)
from random import shuffle

"""
endpoints:
	1)	"/clear_tables"-------->"GET" , "OPTIONS"
	2)	"/populate" ->--------->"GET" , "OPTIONS"
	3)	"/products"	->--------->"GET" , "OPTIONS"

"""




QUESTIONS_PER_PAGE = 10


def paginate_questions(questions_list,pagination):
	#This function will return a 
	#(Paginated, fomatted) list of questions
	min_index=(pagination-1) * QUESTIONS_PER_PAGE
	max_index=(pagination) * QUESTIONS_PER_PAGE
	paginated_formatted_questions_list = list()
	for index,question in enumerate(questions_list):
		if index >= min_index:
			if index < max_index:
				paginated_formatted_questions_list.append(
					question.format())
	return paginated_formatted_questions_list









# Creatng a function to print the error in an approperiate way 
#with detailed info
def my_error(status=404 ,description=""):
	if description == "":
		return jsonify({
					"success": False, 
					"error": status,
					"message": "Not Found",
					}), status
	return jsonify({
			"success": False, 
			"error": status,
			"message": "Not Found",
			"description":description
			}), status





"""
This method searches inside The question model.

Input: String to be searched
Output: Fomatted list of questions matching the search
"""
def question_search(input_text):
	search_query = input_text.strip()
	#To remove the spqce from the beginning and the end of string
	search_query = "%"+search_query+"%"
	all_questions = db.session.query(Question).filter(
		Question.question.ilike(search_query)).all()
	to_return = [question.format() for question in all_questions]
	return to_return




def validate_title(input_t):
	if input_t == None: return [True,None]
	try:
		title = str(input_t)
	except:
		return [False,my_error(status=400, 
			description="title can not be converted to string")]
	if len(title)>100:
		return [False,my_error(status=422, 
			description="maximum title length is 100 letters")]
	return [True,title]




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

		return response
		




	"""
	1)	"/clear_tables"-------->"GET" , "OPTIONS"
	"""
	@app.route("/clear_tables", methods=["GET"])
	def clear_all_tables():
		db.session.rollback()
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
		db.session.rollback()
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
		db.session.rollback()
		in_stock = request.args.get('in_stock')
		print(in_stock, flush=True)
		if in_stock != "false":
			products = get_in_stock_products()
		else:
			products = Product.query.order_by(Product.id).all()
		to_return=[p.simple() for p in products]
		return jsonify({"success":True,"products":to_return})
		






	@app.route("/products", methods=["POST"])
	def post_products():
	#This endpoint will add a new product
		db.session.rollback()
		body = request.get_json()
		try:
			name = body.get("name",None)
			price = body.get("price",None)
			in_stock = body.get("in_stock",None)
			seller = body.get("seller",None)
		except:
			return my_error(status=400, 
				description = "there is no request body")

		title_validation = validate_title(title)
		if title_validation[0]==True:
			title = title_validation[1]
		else:
			return title_validation[1]
		

		recipe_validation = validate_recipe(recipe)
		if recipe_validation[0]==True:
			recipe = recipe_validation[1]
		else:
			return recipe_validation[1]

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