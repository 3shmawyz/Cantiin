"""
Functions:

- my_error(status=404 ,description=""):
- get_in_stock_products()
- validate_product_name(input_n)
- db_drop_and_create_all()
- populate_tables()
- QUESTIONS_PER_PAGE = 10
- def paginate_questions(questions_list,pagination)
- def question_search(input_text)


"""


# Creatng a function to print the error in an approperiate way 
#with detailed info
def my_error(status=404 ,description=""):
	if description == "":
		return jsonify({
					"success": False, 
					"error": status,
					"message": "Not Found",
					}), status
	return jsonify({
			"success": False, 
			"error": status,
			"message": "Not Found",
			"description":description
			}), status














def get_in_stock_products():
    return Product.query.filter(Product.in_stock==True
        ).order_by(Product.id).all()




def validate_product_name(input_n):
	if input_n == None: return [True,None]
	try:
		name = str(input_n)
	except:
		return [False,my_error(status=400, 
			description="name can not be converted to string")]
	if len(name)>100:
		return [False,my_error(status=422, 
			description="maximum name length is 100 letters")]
	return [True,name]



















def db_drop_and_create_all():
    db.drop_all()
    db.create_all()













def populate_tables():
    db_drop_and_create_all()
    products = list()
    
    products.append(Product(
        name="Labtop", price=300, seller="1"))
    products.append(Product(
        name="Mobile", price=100, seller="2", in_stock=False))
    products.append(Product(
        name="Candy", price=.5, seller="3", in_stock=True))
    products.append(Product(
        name="Table", price=150, seller="1", in_stock=False))
    products.append(Product(
        name="Keyboard", price=5, seller="2", in_stock=True))
    products.append(Product(
        name="Mouse", price=4, seller="1", in_stock=True))

    db.session.add_all(products)

    orders = list() 
    #id, user, product, amount
    orders.append(Order(user="1", product=1, amount=1))
    orders.append(Order(user="2", product=1, amount=4))
    orders.append(Order(user="3", product=2, amount=3))
    orders.append(Order(user="1", product=1, amount=2))
    orders.append(Order(user="2", product=2, amount=1))
    orders.append(Order(user="2", product=3, amount=5))
    orders.append(Order(user="1", product=4, amount=20))
    orders.append(Order(user="3", product=5, amount=4))

    db.session.add_all(orders)
    db.session.commit()











QUESTIONS_PER_PAGE = 10


def paginate_questions(questions_list,pagination):
	#This function will return a 
	#(Paginated, fomatted) list of questions
	min_index=(pagination-1) * QUESTIONS_PER_PAGE
	max_index=(pagination) * QUESTIONS_PER_PAGE
	paginated_formatted_questions_list = list()
	for index,question in enumerate(questions_list):
		if index >= min_index:
			if index < max_index:
				paginated_formatted_questions_list.append(
					question.format())
	return paginated_formatted_questions_list









"""
This method searches inside The question model.

Input: String to be searched
Output: Fomatted list of questions matching the search
"""
def question_search(input_text):
	search_query = input_text.strip()
	#To remove the spqce from the beginning and the end of string
	search_query = "%"+search_query+"%"
	all_questions = db.session.query(Question).filter(
		Question.question.ilike(search_query)).all()
	to_return = [question.format() for question in all_questions]
	return to_return



