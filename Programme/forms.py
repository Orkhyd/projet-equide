from models import User

class LoginForm():

	def __init__(self, form):
	    self.login = form['login']
	    

	def validate(self, password):
		user = User(self.login)
		if user.check_password(password):
			return True
		else:
			return False
	
	
