try:
	from .app import create_app
except:
	from app import create_app

application = create_app(testing=False)

if __name__ == '__main__':
	application.run()