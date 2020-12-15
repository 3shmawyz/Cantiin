import os
import unittest
import json
import random
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func 

#from flaskr import create_app
from models import db, populate_tables, db_drop_and_create_all
from flask_cors import CORS
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy
import random


unittest.TestLoader.sortTestMethodsUsing = None

class TriviaTestCase(unittest.TestCase):
	"""This class represents the trivia test case"""

	def setUp(self):
		# create and configure the app
		self.app = create_app() #Flask(__name__)
		self.client = self.app.test_client
		self.app.config.from_object("test")
		db.app = self.app
		db.init_app(self.app)
		db.create_all()        
		
	
	def tearDown(self):
		"""Executed after reach test"""
		print("_+++++++++++++++++++++++++++++++++_")

	#Note: Tests are run alphapetically
	def test_001_test_ot_test(self):
		self.assertEqual(1,1)
		print("Test1: To test that test file is working.")
















# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()