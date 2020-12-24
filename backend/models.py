import os
from sqlalchemy import Column, String, Integer, Float, Boolean
from flask_sqlalchemy import SQLAlchemy
import json


db = SQLAlchemy()

"""
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
"""
'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to 
        have multiple verisons of a database
'''






'''
Product
a persistent product entity, extends the base SQLAlchemy Model
id,name,price,in_stock,seller_id
'''
class User(db.Model):
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

    products = db.relationship("Product",backref="seller")
    orders = db.relationship("Order",backref="buyer")
    #sold_orders = db.relationship("Order",backref="seller")

    def __init__(self, username, password):
        self.username = username
        self.password = password
    '''
    insert()
        inserts a new model into a database
        the model must have a unique username
        the model must have a unique id or null id

    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()
    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
    '''
    def delete(self):
        the_orders=self.orders
        for ord in the_orders:
            ord.delete()
        db.session.delete(self)
        db.session.commit()
    '''
    update()
        updates a new model into a database
        the model must exist in the database
    '''
    def update(self):
        db.session.commit()

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
class Product(db.Model):
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
    seller_id = Column(Integer(),db.ForeignKey("user.id"),
     unique=False, nullable=False)
    #seller_id = Column(Integer(), unique=False, nullable=False)
    # seller_id
    # This is the id of the seller user
    # The user who sells this product
    # it is an integer
    # Example: 1, 2 or 3
    
    orders = db.relationship("Order",backref="product")

    def __init__(self,  
        price, name, seller_id,in_stock=True):
        self.name = name
        self.price = price
        self.in_stock = in_stock
        self.seller_id = seller_id
    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id

    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()
    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
    '''
    def delete(self):
        the_orders=self.orders
        for ord in the_orders:
            ord.delete()
        db.session.delete(self)
        db.session.commit()
    '''
    update()
        updates a new model into a database
        the model must exist in the database
    '''
    def update(self):
        db.session.commit()

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
class Order(db.Model):
    # Autoincrementing, unique primary key
    id = Column(Integer(), primary_key=True)
    # String name
    user_id =Column(Integer(),db.ForeignKey("user.id"),
     unique=False, nullable=False)
    # user_id
    # This is the id of the user who ordered the products
    # it is an integer
    # Example: 1, 2 or 3
    product_id  = Column(Integer,db.ForeignKey("product.id"))
    # product_id is an integer 
    # it refers to the product.id in the products table
    # Example: 1, 2 , 3
    amount =  Column(Integer(), unique=False, nullable=False)
    # amount is an integer
    # Example: 5, 6, 50
    total_cost = 0.0
    def __init__(self, user_id, product_id, amount):
        self.user_id = user_id
        self.product_id = product_id
        self.amount = amount
        self.total_cost= float(amount) * float(Product.query.get(
            product_id).price)

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id

    '''
    def insert(self):
        if self.amount == 0 : 
            return
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            drink = Drink(title=req_title, recipe=req_recipe)
            drink.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database

    '''
    def update(self):
        if self.amount == 0 : 
            db.session.rollback()
            self.delete()
            return
        db.session.commit()

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
 





