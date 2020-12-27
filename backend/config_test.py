import os
import secrets
#SECRET_KEY=os.urandom(32)
SECRET_KEY=secrets.token_urlsafe(5000)
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(
	os.path.join(os.path.dirname(os.path.abspath(__file__)), "databases/test.sqlite"))
SQLALCHEMY_TRACK_MODIFICATIONS= False