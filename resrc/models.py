import os
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, func
import json
from sqlalchemy.orm import backref, relationship, scoped_session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker



Base = declarative_base()
engine = create_engine('sqlite:///databases/test.sqlite', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
										 #autoflush=False,
										 bind=engine))


class NotReceived():
	pass
		


class MyModel():
	#def __init__(self):
	#	pass
	def __init__(self, **kwargs):
		for key in kwargs:
			if type(kwargs[key]) != NotReceived:
				setattr(self,key,kwargs[key])  
	
	def insert(self):
		print(self)
		db_session.add(self)
		db_session.commit()

	def update(self,**kwargs):
		for key in kwargs:
			if type(kwargs[key]) != NotReceived:
				setattr(self,key,kwargs[key])  
		db_session.commit()

	def delete(self):
		db_session.delete(self)
		db_session.commit()
	#def __repr__(self): 
	#	return "Form(%s)" % (', '.join(map(repr, self.args)),)

	def simple(self):
		# Prepare to delete all the keys starting with "_"
		toReturn = {}
		for key in self.__dict__:
			if key[0] == '_':
				continue
			if type(self.__dict__[key]) not in [int,str,float,bool, type(None)]:
				continue
			toReturn[key] = self.__dict__[key]
		return toReturn

	def __repr__(self):
		return json.dumps(self.simple())



'''
User
a persistent product entity, extends the base SQLAlchemy Model
id,username,password

Relationships:
products,orders,images

'''
class User(Base,MyModel):
	#__metaclass__=MyModel
	__tablename__="user"
	# Autoincrementing, unique primary key
	id = Column(Integer(), primary_key=True)
	# String username
	username = Column(String(), unique=True, nullable=False)
	# username could be like "fish"
	# username has to be unique
	# not allowing several users to have the same username
	password =  Column(String(), unique=False, nullable=False)
	# Password is a string
	# Example: "12345", "abc"
	# it doesn't have to be unique

	products = relationship("Product",backref=backref('seller',
						uselist=True,
						cascade='delete,all'))
	orders = relationship("Order",backref=backref('buyer',
						uselist=True,
						cascade='delete,all'))
	images = relationship("Image",backref=backref('seller',
						uselist=True,
						cascade='delete,all'))
	
	"""def simple(self):
		return {
			'id': self.id,
			'username': self.username
		}"""

	def get_dict(self):
		return self.simple()










'''
Product
a persistent product entity, extends the base SQLAlchemy Model
id,name,price,in_stock,seller_id
'''
class Product(Base, MyModel):
	__tablename__="product"
	# Autoincrementing, unique primary key
	id = Column(Integer(), primary_key=True)
	# String name
	name = Column(String(), unique=False, nullable=False)
	# name could be like "Labtop"
	# name dowsn't have to be unique
	# allowing several users to sell the same product
	price =  Column(Float(), unique=False, nullable=False)
	# Price is a float
	# Example: 5.0, 6.0 , 50.0, 0.5
	# It should be float, allowing things with low
	# price to be sold
	in_stock =  Column(Boolean(), unique=False, 
		nullable=False, default=True)
	# in_stock is a boolean
	# Example: True, False
	# it represents whether this product is for sale or not
	# True = For sale, can be displayed to customers
	# False = now for sale, can not be displayed to customers
	seller_id = Column(Integer(),ForeignKey("user.id"),
	 unique=False, nullable=False)
	#seller_id = Column(Integer(), unique=False, nullable=False)
	# seller_id
	# This is the id of the seller user
	# The user who sells this product
	# it is an integer
	# Example: 1, 2 or 3
	def __init__(self,input_dict):
		MyModel.__init__(self,input_dict)
	
	orders = relationship("Order",backref=backref('product',
						uselist=True,
						cascade='delete,all'))


	def __repr__(self):
		return json.dumps(
		{
			'id': self.id,
			'name': self.name,
			'price': self.price,
			'in_stock': self.in_stock,
			'seller_id': self.seller_id
		})
	def simple(self):
		return {
			'id': self.id,
			'name': self.name,
			'price': self.price,
			'in_stock': self.in_stock,
			'seller_id': self.seller_id
		}

	def get_dict(self):
		return self.simple()




"""
Order:
id, user_id, product_id, amount
"""
class Order(Base, MyModel):
	__tablename__="order"
	# Autoincrementing, unique primary key
	id = Column(Integer(), primary_key=True)
	# String name
	user_id =Column(Integer(),ForeignKey("user.id"),
	 unique=False, nullable=False)
	# user_id
	# This is the id of the user who ordered the products
	# it is an integer
	# Example: 1, 2 or 3
	product_id  = Column(Integer,ForeignKey("product.id"))
	# product_id is an integer 
	# it refers to the product.id in the products table
	# Example: 1, 2 , 3
	amount =  Column(Integer(), unique=False, nullable=False)
	# amount is an integer
	# Example: 5, 6, 50
	total_cost = 0.0
	def __init__(self,input_dict):
		MyModel.__init__(self,input_dict)

	def __repr__(self):
		return json.dumps(
		{#id, user_id, product_id, amount

			'id': self.id,
			'user_id': self.user_id,
			'product_id': self.product_id,
			'amount': self.amount,
			"total_cost":float(self.product_id)*float(self.amount)
		})
	def simple(self):
		return {#id, user_id, product_id, amount
			'id': self.id,
			'user_id': self.user_id,
			'amount': self.amount,
			"product_id":self.product_id
		}
 

	def get_dict(self):
		return {#id, user_id, product_id, amount
			'id': self.id,
			'user_id': self.user_id,
			'amount': self.amount,
			"product":self.product.get_dict(),
			"total_cost":self.product.price*float(self.amount)
		}
 










'''
Image
a persistent product entity, extends the base SQLAlchemy Model
id,seller_id,name,formatting

The image will be stroed with it's id
'''
class Image(Base, MyModel):
	__tablename__="image"
	# Autoincrementing, unique primary key
	id = Column(Integer(), primary_key=True)
	seller_id = Column(Integer(),ForeignKey("user.id"),
	 unique=False, nullable=False)
	# This is the id of the seller user
	# The user who sells this product
	# it is an integer
	# Example: 1, 2 or 3
	name = Column(String(), unique=False, nullable=False)
	# image name could be like "fish"
	# image name can not to be unique
	# not allowing several users to have the same username
	formatting =  Column(String(), unique=False, nullable=False)
	# formattng is a string that represents the type of image
	# There can be only 2 types: "png" , "jpg"
	# it can not be unique
	def __init__(self,input_dict):
		MyModel.__init__(self,input_dict)


	def __repr__(self):
		return json.dumps(
		{
			'id': self.id,
			'seller_id': self.seller_id,
			'name': self.name,
			'formatting': self.formatting
		})
	def simple(self):
		return {
			'id': self.id,
			'seller_id': self.seller_id,
			'name': self.name,
			'formatting': self.formatting
		}

	def get_dict(self):
		return self.simple()



def init_db():



	Base.query = db_session.query_property()



	Base.metadata.drop_all(bind=engine)
	Base.metadata.create_all(bind=engine)
init_db()

user = User(username = "abc", password = "123", id = 123)
print(user)
print(user.__dict__)
print(type(user.__dict__["password"]))

#user.insert()
#user.create({"username":123})
#print(user)
#print(dir(user))









