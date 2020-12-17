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






	def test_b_02_001_001_product_exists(self):
		all_products = Product.query
		validation = validate_product_exists(1,all_products)

		self.assertEqual(validation[0],True)
		self.assertEqual(all_products.get(1),validation[1])
		print("Test b_2_1_1: validate_product_exists:correct")
	def test_b_02_001_002_product_exists(self):
		all_products = Product.query
		validation = validate_product_exists(6,all_products)

		self.assertEqual(validation[0],True)
		self.assertEqual(all_products.get(6),validation[1])
		print("Test b_2_1_2: validate_product_exists:correct")






















# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()