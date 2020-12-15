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
	def test_001_test_test(self):
		self.assertEqual(1,1)
		print("Test 1:Hello, Tests!")


	def test_003_test_drop_all_create_all(self):
		db_drop_and_create_all()
		products = Product.query.all()

		self.assertEqual(len(products),0)
		print("Test 2: db_drop_and_create_all")


	def test_003_test_product_insert(self):
		product1 = Product(name = "product1",price = 5.5,
			in_stock=True, seller=1)
		product1.insert()
		products = Product.query.all()

		self.assertEqual(len(products),1)
		print("Test 3: Product insert")


	def test_004_test_product_update(self):
		product1 = Product.query.get(1)
		product1.name = "modified"
		product_1 = Product.query.get(1)

		self.assertEqual(product_1.name,"modified")
		print("Test 4: Product update")



	def test_005_test_product_delete(self):
		product1 = Product.query.get(1)
		product1.delete()
		products = Product.query.all()

		self.assertEqual(len(products),0)
		print("Test 5: Product delete")

	def test_006_test_populate(self):
		populate_tables()
		products = Product.query.all()

		self.assertEqual(len(products),6)
		print("Test 6: Populate Tables")















# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()