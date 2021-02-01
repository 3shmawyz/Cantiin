from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator
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




def validate_string_length_pydantic(the_string:str,minimum:int,maximum:int):
	if len(the_string)<minimum:
		raise ValueError("minimum length of this text is "+ str(minimum))
	if len(the_string)>maximum:
		raise ValueError("maximum length of this text is "+ str(maximum))





class UserPost(BaseModel):
	username:str
	password1:str
	password2:str

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
	password1:str
	password2:str
	
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
	name:str
	price:float
	in_stock:bool=True
	seller_id:int

	@validator
	def name_length(cls,value):
		if length:
			pass

	@validator("price")
	def positive_price(cls,value):
		if value<0.01:
			raise ValueError("minimum price is 0.01")



class ProductPost(BaseModel):
	name:str = NotReceived()
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
	name:str
	formatting:str
	image_b64:str
		
class ImageUpdate(BaseModel):
	seller_id:int = NotReceived()
	name:str = NotReceived()
	formatting:str = NotReceived()
	image_b64:str = NotReceived()
		
	

"""
external_data = {
	'id': '123',
	'signup_ts': '2019-06-01 12:22',
	'friends': [1, 2, '3'],
}
user = User(**external_data)
"""