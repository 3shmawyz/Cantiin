from typing import List, Optional
from pydantic import BaseModel
from models import NotReceived

class UserPost(BaseModel):
	name:str
	password:str
class UserUpdate(BaseModel):
	name:str = NotReceived()
	password:str = NotReceived()

		

"""
external_data = {
	'id': '123',
	'signup_ts': '2019-06-01 12:22',
	'friends': [1, 2, '3'],
}
user = User(**external_data)
"""