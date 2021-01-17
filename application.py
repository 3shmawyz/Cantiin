from src import create_app
application = create_app(testing=False)

"""
Note: The orginal application is packaged inside src directory
You can find the real application there:

src/app.py

When to use this file?
Run this file in production.

python application.py


The best way to run for production from the CLI is like this

export FLASK_APP=app.py
export FLASK_RUN_HOST=127.0.0.1
export FLASK_ENV=development
export FLASK_DEBUG=0
flask run

"""



if __name__ == '__main__':
	application.run()