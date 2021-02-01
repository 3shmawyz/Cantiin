import unittest
from pydantic_models import (UserPost, UserUpdate, ProductPost, 
	ProductPost, OrderPost, OrderUpdate,
	ImagePost, ImageUpdate, validate_model_id,validate_model_id_pydantic)
#from app import create_app
#from models import db
import json
from models import NotReceived, Product, populate_tables
from app import create_app

from pydantic import ValidationError


unittest.TestLoader.sortTestMethodsUsing = None

class pydanticTestCase(unittest.TestCase):
	"""This class represents the trivia test case"""

	def setUp(self):
		#db_drop_and_create_all()
		create_app()
		# create and configure the app
		#self.app = create_app(testing=True) #Flask(__name__)
		#self.client = self.app.test_client
		#db.app = self.app
		#db.init_app(self.app)
		#db.create_all()        
		pass
	
	def tearDown(self):
		"""Executed after reach test"""
		print("_+++++++++++++++++++++++++++++++++_")

	#Note: Tests are run alphapetically
	def test_000001_test(self):
		self.assertEqual(1,1)
		print("Test 1:Hello, Tests!")



	def test_a_1_0_validate_model_id(self):
		populate_tables()
		print("Test b_1_0: validate_model_id Populate")

	def test_a_1_1_validate_model_id(self):
		# Model exists
		self.assertEqual(validate_model_id(Product,1),True)
		# Model does not exist
		self.assertEqual(validate_model_id(Product,10000000000),False)
		try:
			# model is not model
			validate_model_id(123,10000000000)
			self.assertEqual(True,False)
		except Exception as e:
			self.assertEqual(str(e),"validate_model_id:expected the type "+
				"of SQLAlchemy, but found the type of <class 'int'> instead")
		print("Test b_1_1: validate_model_id success")


	def test_a_1_2_validate_model_id_pydantic(self):
		# Model exists: nOo errors raised
		validate_model_id_pydantic(Product,1)
		try:
			# Model does not exist
			self.assertEqual(validate_model_id_pydantic(Product,10000000000),False)
			self.assertEqual(True,False)
		except Exception as e:
			self.assertEqual(str(e),"There is no Product with this id: 10000000000")
		try:
			# model is not model
			validate_model_id(123,10000000000)
			self.assertEqual(True,False)
		except Exception as e:
			self.assertEqual(str(e),"validate_model_id:expected the type "+
				"of SQLAlchemy, but found the type of <class 'int'> instead")
		print("Test b_1_2: validate_model_id success")









	"""def test_b_001_01_1_UserPost(self):
		toValidate = {"username":123,"password":789}
		user = UserPost(**toValidate)
		self.assertEqual(user.dict(),{"username":"123","password":"789"})
		print("Test b_1_1_1:UserPost Successful")

	def test_b_001_01_2_UserPost(self):
		toValidate = {}
		try:
			user = UserPost(**toValidate)
			self.assertEqual(True,False)
		except Exception as e:
			#print(str(e.json()))
			self.assertEqual(json.loads(e.json()),[{"loc": ["username"],
				"msg": "field required","type": "value_error.missing"},{"loc": [
				"password"],"msg": "field required","type": "value_error.missing"}])
		print("Test b_1_1_2:UserPost:Fail:all missing required")

	def test_b_001_01_3_UserPost(self):
		toValidate = {"password":{},"username":{}}
		try:
			user = UserPost(**toValidate)
			self.assertEqual(True,False)
		except Exception as e:
			#print(str(e.json()))
			self.assertEqual(json.loads(e.json()),[{"loc": ["username"],
			"msg": "str type expected","type": "type_error.str"},{"loc": [
	  		"password"],"msg": "str type expected","type": "type_error.str"}])
		print("Test b_1_1_3:UserPost:Fail:username required")






	def test_b_001_02_1_UserUpdate(self):
		toValidate = {"username":123,"password":789}
		user = UserUpdate(**toValidate)
		self.assertEqual(user.dict(),{"username":"123","password":"789"})
		print("Test b_1_2_1:UserUpdate Successful")

	def test_001_02_2_UserUpdate(self):
		toValidate = {"username":123}
		user = UserUpdate(**toValidate)
		self.assertEqual(user.username,"123")
		self.assertEqual(type(user.password),NotReceived)
		#self.assertEqual(user.dict(),{"username":"123","password":NotReceived()})
		print("Test b_1_2_2:UserUpdate Successful Missing field")

	def test_b_001_02_3_UserUpdate(self):
		toValidate = {}
		user = UserUpdate(**toValidate)
		self.assertEqual(type(user.username),NotReceived)
		self.assertEqual(type(user.password),NotReceived)
		print("Test b_1_2_3:UserUpdate Successful: all Missing fields")

	def test_b_001_02_4_UserUpdate(self):
		toValidate = {"password":{},"username":{}}
		try:
			user = UserUpdate(**toValidate)
			self.assertEqual(True,False)
		except Exception as e:
			#print(str(e.json()))
			self.assertEqual(json.loads(e.json()),[{"loc": ["username"],
			"msg": "str type expected","type": "type_error.str"},{"loc": [
	  		"password"],"msg": "str type expected","type": "type_error.str"}])
		print("Test b_1_2_4:UserUpdate:Fail:username required")



















	def test_b_002_01_1_ProductPost(self):
		toValidate = {"username":123,"password":789}
		user = ProductPost(**toValidate)
		self.assertEqual(user.dict(),{"username":"123","password":"789"})
		print("Test b_2_1_1:ProductPost Successful")

	def test_b_002_01_2_ProductPost(self):
		toValidate = {}
		try:
			user = ProductPost(**toValidate)
			self.assertEqual(True,False)
		except Exception as e:
			#print(str(e.json()))
			self.assertEqual(json.loads(e.json()),[{"loc": ["username"],
				"msg": "field required","type": "value_error.missing"},{"loc": [
				"password"],"msg": "field required","type": "value_error.missing"}])
		print("Test b_2_1_2:ProductPost:Fail:all missing required")

	def test_b_002_01_3_ProductPost(self):
		toValidate = {"password":{},"username":{}}
		try:
			user = ProductPost(**toValidate)
			self.assertEqual(True,False)
		except Exception as e:
			#print(str(e.json()))
			self.assertEqual(json.loads(e.json()),[{"loc": ["username"],
			"msg": "str type expected","type": "type_error.str"},{"loc": [
	  		"password"],"msg": "str type expected","type": "type_error.str"}])
		print("Test b_2_1_3:ProductPost:Fail:username required")









	def test_b_002_02_1_ProductUpdate(self):
		toValidate = {"username":123,"password":789}
		user = ProductUpdate(**toValidate)
		self.assertEqual(user.dict(),{"username":"123","password":"789"})
		print("Test b_2_2_1:ProductUpdate Successful")

	def test_b_002_02_2_ProductUpdate(self):
		toValidate = {"username":123}
		user = ProductUpdate(**toValidate)
		self.assertEqual(user.username,"123")
		self.assertEqual(type(user.password),NotReceived)
		#self.assertEqual(user.dict(),{"username":"123","password":NotReceived()})
		print("Test b_2_2_2:ProductUpdate Successful Missing field")

	def test_b_002_02_3_ProductUpdate(self):
		toValidate = {}
		user = ProductUpdate(**toValidate)
		self.assertEqual(type(user.username),NotReceived)
		self.assertEqual(type(user.password),NotReceived)
		print("Test b_2_2_2:ProductUpdate Successful: all Missing fields")

	def test_b_002_02_4_ProductUpdate(self):
		toValidate = {"password":{},"username":{}}
		try:
			user = ProductUpdate(**toValidate)
			self.assertEqual(True,False)
		except Exception as e:
			#print(str(e.json()))
			self.assertEqual(json.loads(e.json()),[{"loc": ["username"],
			"msg": "str type expected","type": "type_error.str"},{"loc": [
	  		"password"],"msg": "str type expected","type": "type_error.str"}])
		print("Test b_2_2_4:ProductUpdate:Fail:username required")"""


































# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()