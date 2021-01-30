import os
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, func
import json
from sqlalchemy.orm import backref, relationship, scoped_session, sessionmaker


from __init__ import (engine, Base, db_session)


class NotReceived():
	pass
		


class MyModel():
	def __init__(self, input_dict):
		for key in input_dict:
			if type(input_dict[key]) != NotReceived:
				setattr(self,"key",input_dict[key])  

	def insert(self):
		db_session.add(self)
		db_session.commit()

	def update(self,input_dict):
		for key in input_dict:
			if type(input_dict[key]) != NotReceived:
				setattr(self,"key",input_dict[key])  
		db_session.commit()

	def delete(self):
		db_session.delete(self)
		db_session.commit()

'''
User
a persistent product entity, extends the base SQLAlchemy Model
id,username,password

Relationships:
products,orders,images

'''
class User(Base):
	__tablename__="users"
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

	def __repr__(self):
		return json.dumps(
		{
			'id': self.id,
			'username': self.username
		})
	def simple(self):
		return {
			'id': self.id,
			'username': self.username
		}

	def get_dict(self):
		return self.simple()










'''
Product
a persistent product entity, extends the base SQLAlchemy Model
id,name,price,in_stock,seller_id
'''
class Product(Base):
	__tablename__="products"
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
class Order(Base):
	__tablename__="orders"
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
class Image(Base):
	__tablename__="images"
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




