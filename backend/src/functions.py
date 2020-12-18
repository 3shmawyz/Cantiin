"""
Functions:

- my_error(status=404 ,description=""):
- get_in_stock_products()






- validate_product_exists(input_id,all_products)
- validate_product_name(input_n)
- validate_product_price(input_p)
- validate_product_in_stock(input_i)
- validate_product_seller(input_s)




- validate_order_exists(input_id,all_orders)
- validate_order_user(input_u)
- validate_order_product(input_id,all_products)
- validate_order_amount(input_a)




- validate_product_name(input_n)
- validate_product_price(imput_p)
- db_drop_and_create_all()
- populate_tables()
- QUESTIONS_PER_PAGE = 10
- def paginate_questions(questions_list,pagination)
- def question_search(input_text)


"""

from models import (db,Product,Order)
import json
from flask import Flask, request, jsonify, abort

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














def get_in_stock_products():
    return Product.query.filter(Product.in_stock==True
        ).order_by(Product.id).all()





"""
This function has 3 inputs:
1)	input_id: an integer, to be valiudated that 
		it exists or not in the table
		Example: 1, 2 or 50
2)	model_query: this is the query of the model
		Example: Product.query, Order.query
3)	name_tring: the name of the table
		Example: "product", "order"

Output:
-	{case,result}
case:1
	-	Successful: passed all the tests
	-	result = correct output
case:2
	- 	Failed:	there was an error while validating
	- 	result:	error message
case:3
	-	Failed input is none
	- 	result:	None
"""
def validate_model_id(input_id,model_query,model_name_string):
	#Validate that model id has a value, not None
	if input_id == None: return {"case":3,"result":None}
	
	#Validate that model id can be converted to int
	try:
		id = int(input_id)
	except:
		return {"case":2,"result":{"status":400, 
			"description":model_name_string+
			" id can not be converted to integer"}} 
		#[False,my_error(status=400, description=model_name_string+" id can not be converted to integer")]
	
	#Validate that id is not negative or zero
	if id<=0:
		return {"case":2,"result":{"status":422, 
			"description":model_name_string+ 
			" id can not be less than"+
			" or equal to 0"}} 

	try:
		item = model_query.get(id)
	except Exception as e:
		return {"case":2,"result":{"status":422, 
			"description":"there is no "+model_name_string+
			+" with this id"}} 
	if item == None :
		return {"case":2,"result":{"status":422, 
			"description":"there is no "+model_name_string
			+" with this id"}} 

	return {"case":1,"result":item}





def validate_string(input_string,max_length,string_name):
	#Validate that input has a value, not None
	if input_string == None: return {"case":3,"result":None}
	
	#Validate that input can be converted to string
	try:
		result = str(input_string)
	except:
		return {"case":2,"result":{"status":400, 
			"description":string_name+
			" can not be converted to string"}} 
	
	#Validate that input length is less that 100
	if len(result)>max_length:
		return {"case":2,"result":{"status":422, 
			"description":"maximum "+ string_name
			+" length is "+str(max_length)+" letters"}} 

	return {"case":1,"result":result}







def validate_boolean(input_i,input_name_string):
	#Validate that product input_i has a value, not None
	if input_i == None: return {"case":3,"result":None}
	
	#Validate that input_i can be converted to boolean

	found_it=False

	if input_i==True or input_i=="true" or input_i=="True" or input_i==1 or input_i=="1":
		found_it=True
		result=True
	if input_i==False or input_i=="false" or input_i=="False" or input_i==0 or input_i=="0":
		found_it=True
		result=False


	if found_it == True:
		return {"case":1,"result":result}
	return {"case":2,"result":{"status":400, 
			"description":input_name_string+" can not be "+
			"converted to boolean"}} 







def validate_integer(
	input_integer,input_name_string,maximum,minimum):
	#Validate that input has a value, not None
	if input_integer == None: return {"case":3,"result":None}
	
	#Validate that input can be converted to int
	try:
		result = int(input_integer)
	except:
		return {"case":2,"result":{"status":400, 
			"description":input_name_string+
			" can not be converted to integer"}} 
	
	#Validate that input is not less than minimum
	if result<int(minimum):
		return {"case":2,"result":{"status":422, 
			"description":input_name_string+
			" can not be less than "+ string(minimum)}} 

	#Validate that input is not more than maximum
	if result>int(maximum):
		return {"case":2,"result":{"status":422, 
			"description":input_name_string+
			" can not be more than "+ string(maximum)}} 
	return {"case":1,"result":result}



def validate_float(
	input_float,input_name_string,maximum,minimum):
	#Validate that input has a value, not None
	if input_float == None: return {"case":3,"result":None}
	
	#Validate that input can be converted to float
	try:
		result = float(input_float)
	except:
		return {"case":2,"result":{"status":400, 
			"description":input_name_string+
			" can not be converted to float"}} 
	
	#Validate that input is not less than minimum
	if result<float(minimum):
		return {"case":2,"result":{"status":422, 
			"description":input_name_string+
			" can not be less than "+ string(minimum)}} 

	#Validate that input is not more than maximum
	if result>float(maximum):
		return {"case":2,"result":{"status":422, 
			"description":input_name_string+
			" can not be more than "+ string(maximum)}} 
	return {"case":1,"result":result}










"""
Product model : inputs validations
"""


def validate_product_exists(input_id,all_products):
	return validate_model_id(input_id,
		all_products,"product")


def validate_product_name(input_n #,all_products
	):
	#Validate that product name has a value, not None
	if input_n == None: return [True,None]
	
	#Validate that product name can be converted to string
	try:
		name = str(input_n)
	except:
		return [False,my_error(status=400, 
			description="name can not be converted to string")]
	
	#Validate that product name length is less that 100
	if len(name)>100:
		return [False,my_error(status=422, 
			description="maximum name length is 100 letters")]

	#Validating that there is no product wth this name already
	"""all_products_names = [p.name.strip().casefold(
		) for p in all_products]
	print(all_products_names,flush=True)
	if name.strip().casefold() in all_products_names:
		return [False,my_error(status=422, 
			description="there is a product"+
			" with this name already")]"""

	return [True,name]


def validate_product_price(input_p):
	#Validate that product price has a value, not None
	if input_p == None: return [True,None]
	
	#Validate that product price can be converted to float
	try:
		price = float(input_p)
	except:
		return [False,my_error(status=400, 
			description="price can not be converted to float")]
	
	#Validate that product price is not negative or zero
	if price<=0:
		return [False,my_error(status=422, 
			description="price can not be less than"+
			" or equal to 0")]

	return [True,price]


def validate_product_in_stock(input_i):
	#Validate that product in_stock has a value, not None
	if input_i == None: return [True,None]
	
	#Validate that product in_stock can be converted to boolean

	found_it=False

	if input_i==True or input_i=="true" or input_i=="True" or input_i==1 or input_i=="1":
		found_it=True
		in_stock=True
	if input_i==False or input_i=="false" or input_i=="False" or input_i==0 or input_i=="0":
		found_it=True
		in_stock=False


	if found_it == True:
		return [True,in_stock]
	return [False,my_error(status=400, 
			description="in_stock can not be "+
			"converted to boolean")]



def validate_product_seller(input_s):
	#Validate that product seller has a value, not None
	if input_s == None: return [True,None]
	
	#Validate that product seller can be converted to float
	try:
		seller = int(input_s)
	except:
		return [False,my_error(status=400, 
			description="seller can not be converted to integer")]
	
	#Validate that product seller is not negative or zero
	if seller<=0:
		return [False,my_error(status=422, 
			description="seller can not be less than"+
			" or equal to 0")]

	#There should be a code to validate that the seller
	#Is in the users table
	return [True,seller]
























"""
Order model : inputs validations
"""

def validate_order_exists(input_id,all_orders):
	return validate_model_id(input_id,
		all_orders,"order")


def validate_order_product(input_id,all_products):
	validate_product_exists(input_id,all_products)


def validate_order_amount(input_a):
	#Validate that order amount has a value, not None
	if input_a == None: return [True,None]
	
	#Validate that order amount can be converted to int
	try:
		amount = int(input_a)
	except:
		return [False,my_error(status=400, 
			description="amount can not be converted to integer")]
	
	#Validate that order amount is not negative or -1
	if amount<=-1:
		return [False,my_error(status=422, 
			description="amount can not be less than"+
			" or equal to -1")]

	return [True,amount]
































def db_drop_and_create_all():
    db.drop_all()
    db.create_all()













def populate_tables():
    db_drop_and_create_all()
    products = list()
    
    products.append(Product(
        name="Labtop", price=300, seller="1"))
    products.append(Product(
        name="Mobile", price=100, seller="2", in_stock=False))
    products.append(Product(
        name="Candy", price=.5, seller="3", in_stock=True))
    products.append(Product(
        name="Table", price=150, seller="1", in_stock=False))
    products.append(Product(
        name="Keyboard", price=5, seller="2", in_stock=True))
    products.append(Product(
        name="Mouse", price=4, seller="1", in_stock=True))

    db.session.add_all(products)

    orders = list() 
    #id, user, product, amount
    orders.append(Order(user="1", product=1, amount=1))
    orders.append(Order(user="2", product=1, amount=4))
    orders.append(Order(user="3", product=2, amount=3))
    orders.append(Order(user="1", product=1, amount=2))
    orders.append(Order(user="2", product=2, amount=1))
    orders.append(Order(user="2", product=3, amount=5))
    orders.append(Order(user="1", product=4, amount=20))
    orders.append(Order(user="3", product=5, amount=4))

    db.session.add_all(orders)
    db.session.commit()











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



