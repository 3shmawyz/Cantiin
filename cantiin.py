from src import create_app
application = create_app(testing=True)


"""
Note: The orginal application is packaged inside src directory
You can find the real application there:

src/app.py

When to use this file?
Run this file in testing on local host.

python cantiin.py

"""


if __name__ == '__main__':
	application.run()