import os
import secrets
#SECRET_KEY=os.urandom(32)
SECRET_KEY=secrets.token_urlsafe(5000)
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True