from typing import List, Optional
from pydantic import BaseModel
from models import NotReceived

class UserPost(BaseModel):
	name:str
	password:str
class UserUpdate(BaseModel):
	name:str = NotReceived()
	password:str = NotReceived()

class ProductPost(object):
	name:str
	price:float
	in_stock:bool=True
	seller_id:int
class ProductPost(object):
	name:str = NotReceived()
	price:float = NotReceived()
	in_stock:bool=NotReceived()
	seller_id:int = NotReceived()
		

"""
external_data = {
	'id': '123',
	'signup_ts': '2019-06-01 12:22',
	'friends': [1, 2, '3'],
}
user = User(**external_data)
"""