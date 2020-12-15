import os
from sqlalchemy import Column, String, Integer
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






def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

'''
Drink
a persistent drink entity, extends the base SQLAlchemy Model
'''
class product(db.Model):
    # Autoincrementing, unique primary key
    id = Column(Integer(), primary_key=True)
    # String Title
    name = Column(String(), unique=True, nullable=False)
    # the ingredients blob - this stores a lazy json blob
    # the required datatype is [{'color': string, 'name':string, 'parts':number}]
    price =  Column(Integer(), unique=False, nullable=False)


    def __init__(self, title, recipe):
        self.title = title
        self.recipe = recipe

    '''
    short()
        short form representation of the Drink model
    '''
    def short(self):
        short_recipe = [{"color": r["color"], "parts": r["parts"]} for r in json.loads(self.recipe)]
        return {
            'id': self.id,
            'title': self.title,
            'recipe': short_recipe
        }

    '''
    long()
        long form representation of the Drink model
    '''
    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'recipe': json.loads(self.recipe)
        }

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            drink = Drink(title=req_title, recipe=req_recipe)
            drink.insert()
    '''
    def insert(self):
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
        EXAMPLE
            drink = Drink.query.filter(Drink.id == id).one_or_none()
            drink.title = 'Black Coffee'
            drink.update()
    '''
    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())







def populate_drink():
    db_drop_and_create_all()
    drinks = list()
    

    drinks.append(Drink(title="Water Cup", recipe=
        '[{'+'"name":"Water","color":"blue","parts":1'+'}]'))
    drinks.append(Drink(title="Nescafe", recipe=
        '['+
        '{'+'"name":"Water","color":"blue","parts":1'+'},'+
        '{'+'"name":"Milk","color":"white","parts":2'+'},'
        '{'+'"name":"Sugar","color":"yellow","parts":1'+'},'
        '{'+'"name":"Nescafe","color":"brown","parts":1'+'}'
        +']'))
    drinks.append(Drink(title="Ice Cream", recipe=
        '['+
        '{'+'"name":"Milk","color":"white","parts":2'+'},'
        '{'+'"name":"Vanillia","color":"white","parts":1'+'},'
        '{'+'"name":"Sugar","color":"white","parts":1'+'}'
        +']'))
    drinks.append(Drink(title="Sugar Cane", recipe=
        '['+
        '{'+'"name":"Cane","color":"yellow","parts":1'+'}'
        +']'))
    drinks.append(Drink(title="Mango Juice", recipe=
        '['+
        '{'+'"name":"MAngo","color":"orange","parts":1'+'}'
        +']'))
    


    db.session.add_all(drinks)
    db.session.commit()

