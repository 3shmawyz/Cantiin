from src import create_app
application = create_app(testing=True)

if __name__ == '__main__':
	application.run()