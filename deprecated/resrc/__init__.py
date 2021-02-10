from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
"""db = SQLAlchemy()
app = Flask("Cantiin")
SQLALCHEMY_DATABASE_URI = "sqlite:///databases/test.sqlite"
SQLALCHEMY_TRACK_MODIFICATIONS= False"""


#from models import User, Product, Order, Image



#Base.metadata.drop_all(bind=engine)
#Base.metadata.create_all(bind=engine)