from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator, constr
from models import NotReceived



"""
validate_model_id
- Inputs:
	- model: the SQLAlchemy model
	- id: the int of the id
- Function:
	- Make sure that this model exists
	- raise error if it was not an integer
- Output:
	- True: This model exists
	- False: This model does not exist
"""

def validate_model_id(model,id:int):
	try:
		if model.query.get(id) == None:
			return False
		return True
	except:
		raise ValueError("validate_model_id:expected the type of SQLAlchemy, but found "+
			"the type of "+str(type(model))+" instead")




"""
validate_model_id_pydantic
- Inputs:
	- model: the SQLAlchemy model
	- id: the int of the id
- Function:
	- raise correct error if the model does not exist
- Output:
	- No output, only error are raised
"""
def validate_model_id_pydantic(model,id:int):
	model_name = model.__name__
	if validate_model_id(model,id) == True:
		pass
	else:
		raise ValueError("There is no "+ model_name + " with this id: " +str(id))




"""
validate_string_length_pydantic
- Inputs:
	- the_string: the string that we want to validate it's length
	- minimum: minimum length of the string
	- maximum: minimum length of the string
- Function:
	- raise correct error if the model does not exist
- Output:
	- No output, only error are raised
"""
def validate_string_length_pydantic(the_string:str,minimum:int,maximum:int):
	if len(the_string)<minimum:
		raise ValueError("minimum length of this text is "+ str(minimum))
	if len(the_string)>maximum:
		raise ValueError("maximum length of this text is "+ str(maximum))





class UserPost(BaseModel):
	username:constr(strip_whitespace=True, min_length=3,max_length=40)
	password1:constr(strip_whitespace=True, min_length=5,max_length=100)
	password2:constr(strip_whitespace=True, min_length=5,max_length=100)

	@validator('username')
	def name_cant_contain_space(cls, value):
		if ' ' in value:
			raise ValueError('username should not contain a space')
		return value

	@validator('password1')
	def passwords_length(cls, value):
		if len(value)<8:
			raise ValueError('minimum password length is 8 characters')
		return value

	@validator('password2')
	def passwords_match(cls, value, values, **kwargs):
		if 'password1' in values and value != values['password1']:
			raise ValueError('passwords do not match')
		return value


class UserUpdate(BaseModel):
	password1:constr(strip_whitespace=True, min_length=5,max_length=100)
	password2:constr(strip_whitespace=True, min_length=5,max_length=100)
	
	@validator('password1')
	def passwords_length(cls, value):
		if len(value)<8:
			raise ValueError('minimum password length is 8 characters')
		return value

	@validator('password2')
	def passwords_match(cls, value, values, **kwargs):
		if 'password1' in values and value != values['password1']:
			raise ValueError('passwords do not match')
		return value










class ProductPost(BaseModel):
	name:constr(strip_whitespace=True, min_length=3,max_length=70)
	price:float
	in_stock:bool=True
	seller_id:int#PositiveInt

	"""@validator
	def name_length(cls,value):
		if length:
			pass"""

	@validator("price")
	def positive_price(cls,value):
		if value<0.01:
			raise ValueError("minimum price is 0.01")



class ProductPost(BaseModel):
	name:constr(strip_whitespace=True, min_length=3,max_length=70) = NotReceived()
	price:float = NotReceived()
	in_stock:bool=NotReceived()
	seller_id:int = NotReceived()


class OrderPost(BaseModel):
	user_id:int
	product_id:int
	amount:int
class OrderUpdate(BaseModel):
	user_id:int = NotReceived()
	product_id:int = NotReceived()
	amount:int = NotReceived()


class ImagePost(BaseModel):
	seller_id:int
	name:constr(strip_whitespace=True, min_length=3,max_length=200)
	formatting:constr(strip_whitespace=True, min_length=2,max_length=15)
	image_b64:constr(strip_whitespace=True, min_length=4,max_length=10000)
		
class ImageUpdate(BaseModel):
	seller_id:int = NotReceived()
	name:constr(strip_whitespace=True, min_length=3,max_length=200)=NotReceived()
	formatting:constr(strip_whitespace=True, min_length=2,max_length=15)=NotReceived()
	image_b64:constr(strip_whitespace=True, min_length=4,max_length=10000)=NotReceived()
		


class TestHere(BaseModel):
	tst:constr(strip_whitespace=True, min_length=1,max_length=5)

"""
external_data = {
	'id': '123',
	'signup_ts': '2019-06-01 12:22',
	'friends': [1, 2, '3'],
}
user = User(**external_data)
"""