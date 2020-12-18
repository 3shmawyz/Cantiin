import os
import unittest
import json
import random
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func 

from api import create_app
from models import (db,Product, Order)
from functions import *
from flask_cors import CORS
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy
import random


"""
a:models
a_01=user
a_02_=product
a_03_=order


b:validation


b:functions
b_01=user validation
b_02=product validation
b_03=order validation


"""

unittest.TestLoader.sortTestMethodsUsing = None

class TriviaTestCase(unittest.TestCase):
	"""This class represents the trivia test case"""

	def setUp(self):
		# create and configure the app
		self.app = create_app(testing=True) #Flask(__name__)
		self.client = self.app.test_client
		#db.app = self.app
		#db.init_app(self.app)
		db.create_all()        
		
	
	def tearDown(self):
		"""Executed after reach test"""
		print("_+++++++++++++++++++++++++++++++++_")

	#Note: Tests are run alphapetically
	def test_001_test(self):
		self.assertEqual(1,1)
		print("Test 1:Hello, Tests!")


	def test_002_drop_all_create_all(self):
		db_drop_and_create_all()
		products = Product.query.all()

		self.assertEqual(len(products),0)
		print("Test 2: db_drop_and_create_all")


	def test_a_2_000_product_intro(self):
		print("")
		print("")
		print("_+++++++++++++++++++++++++++++++++_")
		print("_+++++++++++++++++++ Models : 2 ) Product ++_")
		print("_+++++++++++++++++++++++++++++++++_")
		print("")
		print("")



	def test_a_2_001_product_insert(self):
		product1 = Product(name = "product1",price = 5.5,
			in_stock=True, seller=1)
		product1.insert()
		products = Product.query.all()

		self.assertEqual(len(products),1)
		print("Test a_2_1: Product insert")


	def test_a_2_002_product_update(self):
		product1 = Product.query.get(1)
		product1.name = "modified"
		product1.update()
		product_1 = Product.query.get(1)

		self.assertEqual(product_1.name,"modified")
		print("Test a_2_2: Product update")



	def test_a_2_003_product_delete(self):
		product1 = Product.query.get(1)
		product1.delete()
		products = Product.query.all()

		self.assertEqual(len(products),0)
		print("Test a_2_3: Product delete")

	def test_a_2_004_populate(self):
		populate_tables()
		products = Product.query.all()

		self.assertEqual(len(products),6)
		print("Test a_2_4: Populate Tables")


	def test_a_2_005_product_values(self):
		produc = Product.query.get(1)

		self.assertEqual(produc.id,1)
		self.assertEqual(produc.name,"Labtop")
		self.assertEqual(produc.price,300)
		self.assertEqual(produc.seller,1)
		self.assertEqual(produc.in_stock,True)
		print("Test a_2_5: Product values")


	def test_a_2_006_product_insert_wrong(self):
		products = Product.query.all()
		old_records_number = len(products)
		try:
			#This code will not be executed
			#There are missing required parameters
			product1 = Product()
			product1.insert()
			self.assertEqual(True,False)
		except:
			self.assertEqual(True,True)
		
		products = Product.query.all()
		new_records_number = len(products)

		self.assertEqual(old_records_number,
			new_records_number)
		print("Test a_2_6: product insert with missing"+
		 "required parameters")



	def test_a_2_007_product_delete_wrong(self):
		products = Product.query.all()
		old_records_number = len(products)
		try:
			#This code will not be executed
			#There is no product with the number 0
			product1 = Product.query.get(0)
			product1.delete()
			self.assertEqual(True,False)

		except:
			self.assertEqual(True,True)
		
		products = Product.query.all()
		new_records_number = len(products)

		self.assertEqual(old_records_number,
			new_records_number)
		print("Test a_2_7: product delete mistake, non-existent"+
		 "product id")




	def test_a_2_008_get_in_stock_products(self):
		products = get_in_stock_products()
		for product in products:
			self.assertEqual(product.in_stock,True)
		print("Test a_2_8:get in stock products")



	def test_a_2_009_product_simple(self):
		produc = Product.query.get(1).simple()
		#print(produc)

		self.assertEqual(produc["id"],1)
		self.assertEqual(type(produc["id"]),int)

		self.assertEqual(produc["name"],"Labtop")
		self.assertEqual(type(produc["name"]),str)

		self.assertEqual(produc["price"],300)
		self.assertEqual(type(produc["price"]),float)

		self.assertEqual(produc["seller"],1)
		self.assertEqual(type(produc["seller"]),int)

		self.assertEqual(produc["in_stock"],True)
		self.assertEqual(type(produc["in_stock"]),bool)

		print("Test a_2_9: Product simple")
















	def test_a_3_000_order_intro(self):
		print("")
		print("")
		print("_+++++++++++++++++++++++++++++++++_")
		print("_+++++++++++++++++++ Models : 3 ) Order ++_")
		print("_+++++++++++++++++++++++++++++++++_")
		print("")
		print("")





	def test_a_3_001_odrer_insert(self):
		order1 = Order(user=20, product=5, amount=5)
		order1.insert()
		orders = Order.query.all()

		self.assertEqual(len(orders),9)
		print("Test a_3_1: Order insert")

	def test_a_3_002_odrer_insert_wrong_1(self):
		
		before = len(Order.query.all())
		order1 = Order(user=20, product=5, amount=0)
		order1.insert()
		after = len(Order.query.all())
		self.assertEqual(after,before)
		print("Test a_3_2: Order insert Wrong 1: amount=0")

	def test_a_3_003_odrer_insert_wrong_2(self):
		before = len(Order.query.all())
		try:
			order1 = Order()
			order1.insert()
			self.assertEqual(True,False)
		except:
			self.assertEqual(True,True)
		after = len(Order.query.all())

		self.assertEqual(before,after)
		print("Test a_3_3: Order insert Wrong 2: missing required"+
			" parameters")


	def test_a_3_004_order_update(self):
		order1 = Order.query.get(1)
		order1.amount = 2
		order1.update()
		order_1 = Order.query.get(1)

		self.assertEqual(order_1.amount,2)
		print("Test a_3_4: Order update")

	def test_a_3_005_order_update_wrong(self):
		before = len(Order.query.all())
		order1 = Order.query.get(8)
		order1.amount = 0
		order1.update()
		after = len(Order.query.all())

		self.assertEqual(before,after+1)
		print("Test a_3_5: Order update wrong: amount=0")



	def test_a_3_006_order_delete(self):
		before = len(Order.query.all())
		order1 = Order.query.get(7)
		order1.delete()
		after = len(Order.query.all())

		self.assertEqual(before,after+1)
		print("Test a_3_6: Order delete")


	def test_a_3_007_order_values(self):
		order = Order.query.get(6)

		self.assertEqual(order.id,6)
		self.assertEqual(order.user,2)
		self.assertEqual(order.product,3)
		self.assertEqual(order.amount,5)
		self.assertEqual(order.total_cost,0)
		print("Test a_3_7: Order values")




	def test_a_3_008_order_delete_wrong(self):
		before = len(Order.query.all())
		try:
			#This code will not be executed
			#There is no order with the number 700000
			order = Product.query.get(700000)
			order.delete()
			self.assertEqual(True,False)

		except:
			self.assertEqual(True,True)
		
		after = len(Order.query.all())

		self.assertEqual(before,after)
		print("Test a_3_8: order delete mistake, non-existent"+
		 "order id")




	def test_a_3_009_order_simple(self):
		order = Order.query.get(6).simple()
		#print(produc)

		self.assertEqual(order["id"],6)
		self.assertEqual(type(order["id"]),int)

		self.assertEqual(order["user"],2)
		self.assertEqual(type(order["user"]),int)

		self.assertEqual(order["product"],3)
		self.assertEqual(type(order["product"]),int)

		self.assertEqual(order["amount"],5)
		self.assertEqual(type(order["amount"]),int)

		self.assertEqual(order["total_cost"],2.5)
		self.assertEqual(type(order["total_cost"]),float)

		print("Test a_3_9: Product simple")











	def test_b_01_001_validate_model_id(self):
		all_products = Product.query
		validation = validate_model_id(input_id=1,
			model_query=all_products,
			model_name_string="product")
		self.assertEqual(validation["case"],1)
		self.assertEqual(all_products.get(1),
			validation["result"])
		print("Test b_1_1: validate_model_id: Product 1")


	def test_b_01_002_validate_model_id(self):
		all_products = Product.query
		validation = validate_model_id(input_id=6,
			model_query=all_products,
			model_name_string="product")
		self.assertEqual(validation["case"],1)
		self.assertEqual(all_products.get(6),
			validation["result"])
		print("Test b_1_2: validate_model_id: Product 6")


	def test_b_01_003_validate_model_id(self):
		all_products = Product.query
		validation = validate_model_id(input_id=5.5,
			model_query=all_products,
			model_name_string="product")
		self.assertEqual(validation["case"],1)
		self.assertEqual(all_products.get(5),
			validation["result"])
		print("Test b_1_3: validate_model_id: Product 5.5")


	def test_b_01_004_validate_model_id(self):
		all_products = Product.query
		validation = validate_model_id(input_id="3",
			model_query=all_products,
			model_name_string="product")
		self.assertEqual(validation["case"],1)
		self.assertEqual(all_products.get(3),
			validation["result"])
		print("Test b_1_4: validate_model_id: Product '3'")


	def test_b_01_005_validate_model_id(self):
		all_products = Product.query
		validation = validate_model_id(input_id="i",
			model_query=all_products,
			model_name_string="product")
		self.assertEqual(validation["case"],2)
		self.assertEqual("product id can not be"+
			" converted to integer"
			,validation["result"]["description"])
		self.assertEqual(400
			,validation["result"]["status"])
		print("Test b_1_5: validate_model_id: Product i")


	def test_b_01_006_validate_model_id(self):
		all_products = Product.query
		validation = validate_model_id(input_id=0,
			model_query=all_products,
			model_name_string="product")
		self.assertEqual(validation["case"],2)
		self.assertEqual("product id can not be less than"+
			" or equal to 0"
			,validation["result"]["description"])
		self.assertEqual(422
			,validation["result"]["status"])
		print("Test b_1_6: validate_model_id: Product 0")


	def test_b_01_007_validate_model_id(self):
		all_products = Product.query
		validation = validate_model_id(input_id=-1,
			model_query=all_products,model_name_string="product")
		self.assertEqual(validation["case"],2)
		self.assertEqual("product id can not be less than"+
			" or equal to 0"
			,validation["result"]["description"])
		self.assertEqual(422
			,validation["result"]["status"])
		print("Test b_1_7: validate_model_id: Product -1")


	def test_b_01_008_validate_model_id(self):
		all_products = Product.query
		validation = validate_model_id(input_id=20,
			model_query=all_products,
			model_name_string="product")
		self.assertEqual(validation["case"],2)
		self.assertEqual("there is no product with this id"
			,validation["result"]["description"])
		self.assertEqual(422
			,validation["result"]["status"])
		print("Test b_1_8: validate_model_id: Product 20")


	def test_b_01_009_validate_model_id(self):
		all_products = Product.query
		validation = validate_model_id(input_id=None,
			model_query=all_products,
			model_name_string="product")
		self.assertEqual(validation["case"],3)
		self.assertEqual(None,
			validation["result"])
		print("Test b_1_9: validate_model_id: Product None")


	def test_b_01_010_validate_model_id(self):
		all_orders = Order.query
		validation = validate_model_id(input_id=3,
			model_query=all_orders,
			model_name_string="order")
		self.assertEqual(validation["case"],1)
		self.assertEqual(all_orders.get(3),
			validation["result"])
		print("Test b_1_10: validate_model_id: Order 7")












	def test_b_02_001_validate_string(self):
		to_validate = "to validate"
		validation = validate_string(
			input_string=to_validate,max_length=100,
			string_name="data")
		self.assertEqual(validation["case"],1)
		self.assertEqual("to validate",
			validation["result"])
		print("Test b_2_1: validate_string: 'to validate'")


	def test_b_02_002_validate_string(self):
		to_validate = 1
		validation = validate_string(
			input_string=to_validate,max_length=100,
			string_name="data")
		self.assertEqual(validation["case"],1)
		self.assertEqual("1",
			validation["result"])
		print("Test b_2_2: validate_string: '1'")


	def test_b_02_003_validate_string(self):
		to_validate = "More Than 3"
		validation = validate_string(
		input_string=to_validate,max_length=3,
			string_name="input")		
		self.assertEqual(validation["case"],2)
		self.assertEqual("maximum input length is 3 letters"
			,validation["result"]["description"])
		self.assertEqual(422
			,validation["result"]["status"])
		print("Test b_2_3: validate_string:"+
			" More than max length")


	def test_b_02_004_validate_string(self):
		to_validate = None
		validation = validate_string(
		input_string=to_validate,max_length=3,
			string_name="input")		
		self.assertEqual(validation["case"],3)
		self.assertEqual(validation["result"],None)
		print("Test b_2_4: validate_string:"+
			" None")









	def test_b_3_001_validate_boolean(self):
		validation = validate_boolean(input_boolean=True,
			input_name_string="variable")
		self.assertEqual(validation["case"],1)
		self.assertEqual(True,validation["result"])
		print("Test b_3_1: validate_boolean: True")

	def test_b_3_002_validate_boolean(self):
		validation = validate_boolean(input_boolean="True",
			input_name_string="variable")
		self.assertEqual(validation["case"],1)
		self.assertEqual(True,validation["result"])
		print("Test b_3_2: validate_boolean: 'True'")

	def test_b_3_003_validate_boolean(self):
		validation = validate_boolean(input_boolean="true",
			input_name_string="variable")
		self.assertEqual(validation["case"],1)
		self.assertEqual(True,validation["result"])
		print("Test b_3_3: validate_boolean: 'true'")

	def test_b_3_004_validate_boolean(self):
		validation = validate_boolean(input_boolean=1,
			input_name_string="variable")
		self.assertEqual(validation["case"],1)
		self.assertEqual(True,validation["result"])
		print("Test b_3_4: validate_boolean: 1")

	def test_b_3_005_validate_boolean(self):
		validation = validate_boolean(input_boolean="1",
			input_name_string="variable")
		self.assertEqual(validation["case"],1)
		self.assertEqual(True,validation["result"])
		print("Test b_3_5: validate_boolean: '1'")

	def test_b_3_006_validate_boolean(self):
		validation = validate_boolean(input_boolean=False,
			input_name_string="variable")
		self.assertEqual(validation["case"],1)
		self.assertEqual(False,validation["result"])
		print("Test b_3_6: validate_boolean: False")

	def test_b_3_007_validate_boolean(self):
		validation = validate_boolean(input_boolean="False",
			input_name_string="variable")
		self.assertEqual(validation["case"],1)
		self.assertEqual(False,validation["result"])
		print("Test b_3_7: validate_boolean: 'False'")

	def test_b_3_008_validate_boolean(self):
		validation = validate_boolean(input_boolean="false",
			input_name_string="variable")
		self.assertEqual(validation["case"],1)
		self.assertEqual(False,validation["result"])
		print("Test b_3_8: validate_boolean: 'false'")

	def test_b_3_009_validate_boolean(self):
		validation = validate_boolean(input_boolean=0,
			input_name_string="variable")
		self.assertEqual(validation["case"],1)
		self.assertEqual(False,validation["result"])
		print("Test b_3_9: validate_boolean: 0")

	def test_b_3_010_validate_boolean(self):
		validation = validate_boolean(input_boolean="0",
			input_name_string="variable")
		self.assertEqual(validation["case"],1)
		self.assertEqual(False,validation["result"])
		print("Test b_3_10: validate_boolean: '0'")

	def test_b_3_011_validate_boolean_wrong(self):
		validation = validate_boolean(input_boolean="5",
			input_name_string="variable")
		self.assertEqual(validation["case"],2)
		self.assertEqual("variable can not be "+
			"converted to boolean"
			,validation["result"]["description"])
		self.assertEqual(400
			,validation["result"]["status"])
		print("Test b_3_11: validate_boolean_wrong:"+
			" '5'")

	def test_b_3_012_validate_boolean(self):
		validation = validate_boolean(input_boolean=None,
			input_name_string="variable")
		self.assertEqual(validation["case"],3)
		self.assertEqual(None,validation["result"])
		print("Test b_3_12: validate_boolean: None")






















	def test_b_05_001_validate_float(self):
		validation = validate_float(input_float=5,
			input_name_string="input",maximum=1000,
			minimum=0)

		self.assertEqual(validation["case"],1)
		self.assertEqual(5.0,validation["result"])
		print("Test b_5_1: validate_float: 5")

	def test_b_05_002_validate_float(self):
		validation = validate_float(input_float=5.0,
			input_name_string="input",maximum=1000,
			minimum=0)

		self.assertEqual(validation["case"],1)
		self.assertEqual(5.0,validation["result"])
		print("Test b_5_2: validate_float: 5.0")

	def test_b_05_003_validate_float(self):
		validation = validate_float(input_float="5.0",
			input_name_string="input",maximum=1000,
			minimum=0)

		self.assertEqual(validation["case"],1)
		self.assertEqual(5.0,validation["result"])
		print("Test b_5_3: validate_float: '5.0'")

	def test_b_05_004_validate_float_wrong(self):
		validation = validate_float(input_float="i",
			input_name_string="input",maximum=1000,
			minimum=0)

		self.assertEqual(validation["case"],2)
		self.assertEqual("input can not be converted to float"
			,validation["result"]["description"])
		self.assertEqual(400
			,validation["result"]["status"])
		print("Test b_5_4: validate_float: i")

	def test_b_05_005_validate_float_wrong(self):
		validation = validate_float(input_float=0,
			input_name_string="input",maximum=1000,
			minimum=0)

		self.assertEqual(validation["case"],2)
		self.assertEqual("input can not be less than"+
			" or equal to 0"
			,validation["result"]["description"])
		self.assertEqual(422
			,validation["result"]["status"])
		print("Test b_5_5: validate_float: 0")

	def test_b_05_006_validate_float_wrong(self):
		validation = validate_float(input_float=-40,
			input_name_string="input",maximum=1000,
			minimum=0)

		self.assertEqual(validation["case"],2)
		self.assertEqual("input can not be less than"+
			"  0"
			,validation["result"]["description"])
		self.assertEqual(422
			,validation["result"]["status"])
		print("Test b_5_6: validate_float: -40")














	def test_b_02_002_001_product_name(self):
		validation = validate_product_name("Hi There")
		self.assertEqual(validation[0],True)
		self.assertEqual("Hi There",validation[1])
		print("Test b_2_2_1: validate_product_Name: Hi There")

	def test_b_02_002_002_product_name(self):
		validation = validate_product_name(1)

		self.assertEqual(validation[0],True)
		self.assertEqual("1",validation[1])
		print("Test b_2_2_2: validate_product_Name: 1")

	def test_b_02_002_003_product_name_wrong(self):
		validation = validate_product_name('1111111'+
			"111111111111111111111111111111111111111"+
			"111111111111111111111111111111111111111"+
			"111111111111111111111111111111111111111"+
			"111111111111111111111111111111111111111"+
			"111111111111111111111111111111111111111"+
			"111111111111111111111111111111111111111"+
			"111111111111111111111111111111111111111"+
			"111111111111111111111111111111111111111"+
			"111111111111111111111111111111111111111")
		self.assertEqual(validation[0],False)
		self.assertEqual("maximum name length is 100 letters"
			,validation[1][0]["description"])
		self.assertEqual(422
			,validation[1][1])
		print("Test b_2_2_3: validate_product_Name:"+
			"very long name")



	def test_b_02_003_001_product_price(self):
		validation = validate_product_price(5)

		self.assertEqual(validation[0],True)
		self.assertEqual(5.0,validation[1])
		print("Test b_2_3_1: validate_product_price: 5")

	def test_b_02_003_002_product_price(self):
		validation = validate_product_price(5.0)

		self.assertEqual(validation[0],True)
		self.assertEqual(5.0,validation[1])
		print("Test b_2_3_2: validate_product_price: 5.0")

	def test_b_02_003_003_product_price(self):
		validation = validate_product_price("5.0")

		self.assertEqual(validation[0],True)
		self.assertEqual(5.0,validation[1])
		print("Test b_2_3_3: validate_product_price: '5.0'")

	def test_b_02_003_004_product_price_wrong(self):
		validation = validate_product_price("i")

		self.assertEqual(validation[0],False)
		self.assertEqual("price can not be converted to float"
			,validation[1][0]["description"])
		self.assertEqual(400
			,validation[1][1])
		print("Test b_2_3_4: validate_product_price: i")

	def test_b_02_003_005_product_price_wrong(self):
		validation = validate_product_price(0)

		self.assertEqual(validation[0],False)
		self.assertEqual("price can not be less than"+
			" or equal to 0"
			,validation[1][0]["description"])
		self.assertEqual(422
			,validation[1][1])
		print("Test b_2_3_5: validate_product_price: 0")

	def test_b_02_003_006_product_price_wrong(self):
		validation = validate_product_price(-40)

		self.assertEqual(validation[0],False)
		self.assertEqual("price can not be less than"+
			" or equal to 0"
			,validation[1][0]["description"])
		self.assertEqual(422
			,validation[1][1])
		print("Test b_2_3_6: validate_product_price: -40")








	def test_b_02_004_001_product_validate_boolean(self):
		validation = validate_product_in_stock(True)
		self.assertEqual(validation[0],True)
		self.assertEqual(True,validation[1])
		print("Test b_2_4_1: validate_product_in_stock: True")

	def test_b_02_004_002_product_validate_boolean(self):
		validation = validate_product_in_stock("True")
		self.assertEqual(validation[0],True)
		self.assertEqual(True,validation[1])
		print("Test b_2_4_2: validate_product_in_stock: 'True'")

	def test_b_02_004_003_product_validate_boolean(self):
		validation = validate_product_in_stock("true")
		self.assertEqual(validation[0],True)
		self.assertEqual(True,validation[1])
		print("Test b_2_4_3: validate_product_in_stock: 'true'")

	def test_b_02_004_004_product_validate_boolean(self):
		validation = validate_product_in_stock(1)
		self.assertEqual(validation[0],True)
		self.assertEqual(True,validation[1])
		print("Test b_2_4_4: validate_product_in_stock: 1")

	def test_b_02_004_005_product_validate_boolean(self):
		validation = validate_product_in_stock("1")
		self.assertEqual(validation[0],True)
		self.assertEqual(True,validation[1])
		print("Test b_2_4_5: validate_product_in_stock: '1'")



	def test_b_02_004_006_product_validate_boolean(self):
		validation = validate_product_in_stock(False)
		self.assertEqual(validation[0],True)
		self.assertEqual(False,validation[1])
		print("Test b_2_4_6: validate_product_in_stock: False")

	def test_b_02_004_007_product_validate_boolean(self):
		validation = validate_product_in_stock("False")
		self.assertEqual(validation[0],True)
		self.assertEqual(False,validation[1])
		print("Test b_2_4_7: validate_product_in_stock: 'False'")

	def test_b_02_004_008_product_validate_boolean(self):
		validation = validate_product_in_stock("false")
		self.assertEqual(validation[0],True)
		self.assertEqual(False,validation[1])
		print("Test b_2_4_8: validate_product_in_stock: 'false'")

	def test_b_02_004_009_product_validate_boolean(self):
		validation = validate_product_in_stock(0)
		self.assertEqual(validation[0],True)
		self.assertEqual(False,validation[1])
		print("Test b_2_4_9: validate_product_in_stock: 0")

	def test_b_02_004_010_product_validate_boolean(self):
		validation = validate_product_in_stock("0")
		self.assertEqual(validation[0],True)
		self.assertEqual(False,validation[1])
		print("Test b_2_4_10: validate_product_in_stock: '0'")


	def test_b_02_004_010_product_validate_boolean_wrong(self):
		validation = validate_product_in_stock("5")
		self.assertEqual(validation[0],False)
		self.assertEqual("in_stock can not be "+
			"converted to boolean"
			,validation[1][0]["description"])
		self.assertEqual(400
			,validation[1][1])
		print("Test b_2_4_10: validate_product_in_stock_wrong:"+
			" '5'")










	def test_b_02_005_001_product_seller(self):
		validation = validate_product_seller(1)
		self.assertEqual(validation[0],True)
		self.assertEqual(1,validation[1])
		print("Test b_2_5_1: validate_product_seller: 1")

	def test_b_02_005_002_product_seller(self):
		validation = validate_product_seller("1")
		self.assertEqual(validation[0],True)
		self.assertEqual(1,validation[1])
		print("Test b_2_5_2: validate_product_seller: '1'")

	def test_b_02_005_003_product_seller(self):
		validation = validate_product_seller(1.5)
		self.assertEqual(validation[0],True)
		self.assertEqual(1,validation[1])
		print("Test b_2_5_3: validate_product_seller: 1.5")

	def test_b_02_005_004_product_seller_wrong(self):
		validation = validate_product_seller("i")
		self.assertEqual(validation[0],False)
		self.assertEqual("seller can not be converted to integer"
			,validation[1][0]["description"])
		self.assertEqual(400
			,validation[1][1])
		print("Test b_2_5_4: validate_product_seller_wrong: 1.5")

	def test_b_02_005_005_product_seller_wrong(self):
		validation = validate_product_seller(0)
		self.assertEqual(validation[0],False)
		self.assertEqual("seller can not be less than"+
			" or equal to 0"
			,validation[1][0]["description"])
		self.assertEqual(422
			,validation[1][1])
		print("Test b_2_5_5: validate_product_seller_wrong: 0")

	def test_b_02_005_006_product_seller_wrong(self):
		validation = validate_product_seller(-1)
		self.assertEqual(validation[0],False)
		self.assertEqual("seller can not be less than"+
			" or equal to 0"
			,validation[1][0]["description"])
		self.assertEqual(422
			,validation[1][1])
		print("Test b_2_5_6: validate_product_seller_wrong: -1")

	def test_b_02_005_007_product_seller_wrong(self):
		validation = validate_product_seller("-1")
		self.assertEqual(validation[0],False)
		self.assertEqual("seller can not be less than"+
			" or equal to 0"
			,validation[1][0]["description"])
		self.assertEqual(422
			,validation[1][1])
		print("Test b_2_5_7: validate_product_seller_wrong: '-1'")



















	def test_b_02_003_001_order_exists(self):
		all_orders = Order.query
		validation = validate_order_exists(1,all_orders)

		self.assertEqual(validation[0],True)
		self.assertEqual(all_orders.get(1),validation[1])
		print("Test b_2_3_1: validate_order_exists:1")

	def test_b_02_003_002_order_exists(self):
		all_orders = Order.query
		validation = validate_order_exists(6,all_orders)

		self.assertEqual(validation[0],True)
		self.assertEqual(all_orders.get(6),validation[1])
		print("Test b_2_3_2: validate_order_exists:6")

	def test_b_02_003_003_order_exists_float(self):
		all_orders = Order.query
		validation = validate_order_exists(5.5,all_orders)

		self.assertEqual(validation[0],True)
		self.assertEqual(all_orders.get(5),validation[1])
		print("Test b_2_3_3: validate_order_exists:5.5")

	def test_b_02_003_004_order_exists_string(self):
		all_orders = Order.query
		validation = validate_order_exists("3",all_orders)

		self.assertEqual(validation[0],True)
		self.assertEqual(all_orders.get(3),validation[1])
		print("Test b_2_3_4: validate_order_exists:'3'")

	def test_b_02_003_005_order_exists_wrong(self):
		all_orders = Order.query
		validation = validate_order_exists("i",all_orders)

		self.assertEqual(validation[0],False)
		self.assertEqual("id can not be converted to integer"
			,validation[1][0]["description"])
		self.assertEqual(400
			,validation[1][1])
		print("Test b_2_3_5: validate_order_exists:i")

	def test_b_02_003_006_order_exists_wrong(self):
		all_orders = Order.query
		validation = validate_order_exists(0,all_orders)

		self.assertEqual(validation[0],False)
		self.assertEqual("id can not be less than"+
			" or equal to 0",validation[1][0]["description"])
		self.assertEqual(422
			,validation[1][1])
		print("Test b_2_3_6: validate_order_exists:0")

	def test_b_02_003_007_order_exists_wrong(self):
		all_orders = Order.query
		validation = validate_order_exists(-1,all_orders)

		self.assertEqual(validation[0],False)
		self.assertEqual("id can not be less than"+
			" or equal to 0",validation[1][0]["description"])
		self.assertEqual(422
			,validation[1][1])
		print("Test b_2_3_7: validate_order_exists:-1")

	def test_b_02_003_008_order_exists_wrong(self):
		all_orders = Order.query
		validation = validate_order_exists(20,all_orders)

		self.assertEqual(validation[0],False)
		self.assertEqual("there is no order with this id"
			,validation[1][0]["description"])
		self.assertEqual(422
			,validation[1][1])
		print("Test b_2_3_8: validate_order_exists:20")






















# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()