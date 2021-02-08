from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator, constr, conint, confloat
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

# General
id_con = conint(gt=0)


# User
username_con = constr(strip_whitespace=True, min_length=3,max_length=40)
password_con = constr(strip_whitespace=True, min_length=5,max_length=100)

#Product Name
product_name_con = constr(strip_whitespace=True, min_length=3,max_length=100)
product_price_con = confloat(ge=.1, le=1000000)


# Order
amount_con = conint(gt=-1, lt=100)

#Image
image_name_con = constr(strip_whitespace=True, min_length=3,max_length=200)
formatting_con = constr(strip_whitespace=True, min_length=2,max_length=15)
image_b64_con = constr(strip_whitespace=True, min_length=4,max_length=10000)


class UserPost(BaseModel):
	username : username_con
	password1 : password_con
	password2 : password_con

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
	password1 : password_con
	password2 : password_con
	
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
	name : product_name_con
	price : product_price_con
	in_stock : bool=True

	@validator("price")
	def positive_price(cls,value):
		if value<0.01:
			raise ValueError("minimum price is 0.01")



class ProductUpdate(BaseModel):
	name : product_name_con = NotReceived()
	price : product_price_con = NotReceived()
	in_stock : bool = NotReceived()


class OrderPost(BaseModel):
	product_id : id_con
	amount : amount_con
class OrderUpdate(BaseModel):
	product_id : id_con = NotReceived()
	amount : amount_con = NotReceived()


class ImagePost(BaseModel):
	name :  image_name_con
	formatting : formatting_con
	image_b64 : image_b64_con 

class ImageUpdate(BaseModel):
	name : image_name_con = NotReceived()
	formatting : formatting_con = NotReceived()
	image_b64 : image_b64_con = NotReceived()
		



the_tst=constr(strip_whitespace=True, min_length=1,max_length=5)
		


class TestHere(BaseModel):
	tst:the_tst

"""
external_data = {
	'id': '123',
	'signup_ts': '2019-06-01 12:22',
	'friends': [1, 2, '3'],
}
user = User(**external_data)
"""