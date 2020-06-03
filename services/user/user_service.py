import utilities.crypto

from settings.db import Database
from domain.user import User


class UserService:
	def __init__(self):
		self.database = Database()

	def create_user(self, user=None):
		# create new user
		# user is an User instance
		try:
			sql = '''
				INSERT INTO users(id, username, password, role)
				VALUES('%s', '%s', '%s', '%s')
			''' % user.id, user.username, user.password, user.role
			self.database.execute(sql)
			return None
		except Exception as e:
			return e

	def login(self, user):
		# user try to login
		# user is an User instance
		sql = '''
			SELECT id, username, password, role FROM users
			WHERE username = '%s' AND password = '%s'
		''' % (user.username, user.password)
		results = self.database.query(sql)
		for result in results:
			user = User()
			user.scan(result)
			token = utilities.crypto.encode_jwt_token(user.ser())
			return token

		return Exception('wrong username or password')
