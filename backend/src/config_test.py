import os
SECRET_KEY=os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(
	os.path.join(os.path.dirname(os.path.abspath(__file__)), "test.db"))
SQLALCHEMY_TRACK_MODIFICATIONS= False