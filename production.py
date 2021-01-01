from src.app import *
application = create_app(testing=False)

if __name__ == '__main__':
	application.run()