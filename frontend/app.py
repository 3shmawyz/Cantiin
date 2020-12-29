#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
import traceback
import json
import dateutil.parser
import babel
import sys,os
import logging
import datetime
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from forms import *
from logging import Formatter, FileHandler
from sqlalchemy import func
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField,BooleanField,RadioField
from wtforms.validators import DataRequired, AnyOf, URL



app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate=Migrate (app,db)










if __name__=="__main__":
    app.run(port=8000)