import os
import unittest
import json
import random
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func 

from api import create_app
from models import (db, populate_tables, db_drop_and_create_all,
Product)
from flask_cors import CORS
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy
import random


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


	def test_003_drop_all_create_all(self):
		db_drop_and_create_all()
		products = Product.query.all()

		self.assertEqual(len(products),0)
		print("Test 2: db_drop_and_create_all")


	def test_003_product_insert(self):
		product1 = Product(name = "product1",price = 5.5,
			in_stock=True, seller=1)
		product1.insert()
		products = Product.query.all()

		self.assertEqual(len(products),1)
		print("Test 3: Product insert")


	def test_004_product_update(self):
		product1 = Product.query.get(1)
		product1.name = "modified"
		product_1 = Product.query.get(1)

		self.assertEqual(product_1.name,"modified")
		print("Test 4: Product update")



	def test_005_product_delete(self):
		product1 = Product.query.get(1)
		product1.delete()
		products = Product.query.all()

		self.assertEqual(len(products),0)
		print("Test 5: Product delete")

	def test_006_populate(self):
		populate_tables()
		products = Product.query.all()

		self.assertEqual(len(products),6)
		print("Test 6: Populate Tables")


	def test_007_product_values(self):
		produc = Product.query.get(1)

		self.assertEqual(produc.id,1)
		self.assertEqual(produc.name,"Labtop")
		self.assertEqual(produc.price,300)
		self.assertEqual(produc.seller,1)
		self.assertEqual(produc.in_stock,True)
		print("Test 7: Product values")


	def test_008_product_insert_wrong(self):
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
		print("Test8: product insert with missing"+
		 "required parameters")



	def test_009_product_delete_wrong(self):
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
		print("Test9: product delete mistake, non-existent"+
		 "product id")




	def test_010_get_in_stock_products(self):
		products = get_in_stock_products()
		for product in products:
			self.assertEqual(product.in_stock,True)
		print("Test10:get in stock products")













# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()