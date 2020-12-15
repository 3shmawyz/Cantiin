import os
import unittest
import json
import random
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func 

from api import create_app
from models import (db, populate_tables, db_drop_and_create_all,
Product, get_in_stock_products)
from flask_cors import CORS
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy
import random


"""
a:models
a_01=user
a_02_=product
a_03_=order
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


	def test_a_1_001_product_insert(self):
		product1 = Product(name = "product1",price = 5.5,
			in_stock=True, seller=1)
		product1.insert()
		products = Product.query.all()

		self.assertEqual(len(products),1)
		print("Test a_1_1: Product insert")


	def test_a_1_002_product_update(self):
		product1 = Product.query.get(1)
		product1.name = "modified"
		product_1 = Product.query.get(1)

		self.assertEqual(product_1.name,"modified")
		print("Test a_1_2: Product update")



	def test_a_1_003_product_delete(self):
		product1 = Product.query.get(1)
		product1.delete()
		products = Product.query.all()

		self.assertEqual(len(products),0)
		print("Test a_1_3: Product delete")

	def test_a_1_004_populate(self):
		populate_tables()
		products = Product.query.all()

		self.assertEqual(len(products),6)
		print("Test a_1_4: Populate Tables")


	def test_a_1_005_product_values(self):
		produc = Product.query.get(1)

		self.assertEqual(produc.id,1)
		self.assertEqual(produc.name,"Labtop")
		self.assertEqual(produc.price,300)
		self.assertEqual(produc.seller,1)
		self.assertEqual(produc.in_stock,True)
		print("Test a_1_5: Product values")


	def test_a_1_006_product_insert_wrong(self):
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
		print("Test a_1_6: product insert with missing"+
		 "required parameters")



	def test_a_1_007_product_delete_wrong(self):
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
		print("Test a_1_7: product delete mistake, non-existent"+
		 "product id")




	def test_a_1_008_get_in_stock_products(self):
		products = get_in_stock_products()
		for product in products:
			self.assertEqual(product.in_stock,True)
		print("Test a_1_8:get in stock products")



	def test_a_1_009_product_simple(self):
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

		print("Test a_1_9: Product simple")













# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()