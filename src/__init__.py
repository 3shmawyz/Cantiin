from datetime import timedelta
import secrets
from flask_sqlalchemy import SQLAlchemy


EXPIRATION_AFTER= timedelta(days=7)
SECRET=str(secrets.token_urlsafe(5000))
db = SQLAlchemy()

try:
	from .models import (db, Product, Order,User)
	from .functions import *
	from .auth import *
	from .app import *
	from .test import *
except:
	from models import (db, Product, Order,User)
	from functions import *
	from auth import *
	from app import *
