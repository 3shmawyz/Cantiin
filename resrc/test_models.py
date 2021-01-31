




unittest.TestLoader.sortTestMethodsUsing = None

class modelsTestCase(unittest.TestCase):
	"""This class represents the trivia test case"""

	def setUp(self):
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
	def test_001_test(self):
		self.assertEqual(1,1)
		print("Test 1:Hello, Tests!")











# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()