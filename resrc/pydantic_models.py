from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator
from models import NotReceived



def validate_model_id(model,id):
	try:
		model.query.get(id)
		return True
	except Exception as e:
		return False






class UserPost(BaseModel):
	username:str
	password1:str
	password2:str
	
	@validator('password2')
	def passwords_match(cls, v, values, **kwargs):
		if 'password1' in values and v != values['password1']:
			raise ValueError('passwords do not match')
		return v



class UserUpdate(BaseModel):
	password1:str
	password2:str

	@validator('password2')
	def passwords_match(cls, v, values, **kwargs):
		if 'password1' in values and v != values['password1']:
			raise ValueError('passwords do not match')
		return v



class ProductPost(BaseModel):
	name:str
	price:float
	in_stock:bool=True
	seller_id:int



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