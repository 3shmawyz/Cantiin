import unittest
from pydantic_models import (UserPost, UserUpdate, ProductPost, ProductPost, OrderPost, OrderUpdate,
	ImagePost, ImageUpdate)
#from app import create_app
#from models import db
import json

unittest.TestLoader.sortTestMethodsUsing = None

class pydanticTestCase(unittest.TestCase):
	"""This class represents the trivia test case"""

	def setUp(self):
		#db_drop_and_create_all()
		#create_app()
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


	def test_001_01_1_UserPost(self):
		toValidate = {"username":123,"password":789}
		user = UserPost(**toValidate)
		self.assertEqual(user.dict(),{"username":"123","password":"789"})
		print("Test 1_1_1:UserPost Successful")

	def test_001_01_2_UserPost(self):
		toValidate = {}
		try:
			user = UserPost(**toValidate)
			self.assertEqual(True,False)
		except Exception as e:
			#print(str(e.json()))
			self.assertEqual(json.loads(e.json()),[{"loc": ["username"],
				"msg": "field required","type": "value_error.missing"},{"loc": [
				"password"],"msg": "field required","type": "value_error.missing"}])
		print("Test 1_1_2:UserPost:Fail:all missing required")

	def test_001_01_3_UserPost(self):
		toValidate = {"password":{},"username":{}}
		try:
			user = UserPost(**toValidate)
			self.assertEqual(True,False)
		except Exception as e:
			#print(str(e.json()))
			self.assertEqual(json.loads(e.json()),[{"loc": ["username"],
			"msg": "str type expected","type": "type_error.str"},{"loc": [
	  		"password"],"msg": "str type expected","type": "type_error.str"}])
		print("Test 1_1_3:UserPost:Fail:username required")



































# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()