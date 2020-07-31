from utilities.time import Time
from utilities.unique import Unique
from utilities.crypto import Crypto
from utilities.crypto import InvalidToken


class User:
	def __init__(self, email=None, password=None):
		self.id = None
		self.email = email
		self.password = password
		self.created_at = None
		self.deleted_at = None
		self.last_access = None
		self.github_token = None

	def __ser__(self):
		return {
			'id': self.id,
			'email': self.email
		}

	def __str__(self):
		return str(self.__ser__())

	def ser(self):
		return self.__ser__()

	def create(self):
		self.id = Unique.generate_id()
		self.created_at = self.last_access = Time.current_timestamp()
		self.password = Crypto.hash_password(self.password)

	def set_github_token(self, token=None):
		self.github_token = token

	def encode(self):
		"""
		Encode user data into a JWT token
		:return: JWT token
		"""
		data = self.ser()
		data['expired'] = Time.get_token_expired()
		return Crypto.encode_jwt_token(data=data)

	@staticmethod
	def decode(token):
		if token is None:
			return InvalidToken
		ser_data = Crypto.decode_jwt_token(token)
		if ser_data is None:
			user = User.scan(ser_data)
			return user
		else:
			return ser_data

	@staticmethod
	def scan(raw_data):
		"""
		Scan a raw dictionary data present user data into User object
		:param raw_data: a dictionary present user data
		:return:
		"""
		if 'password' in raw_data:
			password = raw_data['password']
		else:
			password = None

		user = User(email=raw_data['email'], password=password)
		user.id = raw_data['id']

		if 'github' in raw_data:
			if 'token' in raw_data['github']:
				user.github_token = raw_data['github']['token']

		if 'audit' in raw_data:
			if 'created_at' in raw_data['audit']:
				user.created_at = raw_data['audit']['created_at']
			if 'deleted_at' in raw_data['audit']:
				user.deleted_at = raw_data['audit']['deleted_at']
			if 'last_access' in raw_data['audit']:
				user.last_access = raw_data['audit']['last_access']
		return user

	@staticmethod
	def compose(raw_data):
		"""
		Compose an User from raw data
		:param raw_data: a dictionary present user email, password and github token
		:return:
		"""
		user = User(email=raw_data['email'], password=raw_data['password'])
		user.create()
		if 'github' in raw_data:
			if 'token' in raw_data['github']:
				user.set_github_token(raw_data['github']['token'])
		return user


class TestUser:
	def __init__(self):
		self.test_case = {
			'email': 'example@gmail.com',
			'password': 'hello',
			'github': {
				'token': 'example_token'
			}
		}
		self.user = None

	def __create_user__(self):
		self.user = User.compose(self.test_case)
		self.test_case['id'] = self.user.id

		assert self.user is not None, 'user must be not None, got %s' % str(self.user)
		assert self.user.email == self.test_case['email'], 'expected email: %s, got %s' % (self.test_case['email'], self.user.email)

		expected_password = Crypto.hash_password(self.test_case['password'])
		assert self.user.password == expected_password, 'expected password: %s, got %s' % (expected_password, self.user.password)

		assert self.user.created_at is not None, 'expected created_at is not None'
		assert self.user.deleted_at is None, 'expected deleted_at is None'
		assert self.user.last_access is not None, 'expected last_access is not None'
		assert self.user.github_token == self.test_case['github']['token'], 'expected github token: %s, got %s' % (self.test_case['gihub']['token'], self.user.github_token)

	def __token__(self):
		token = self.user.encode()
		assert token is not None, 'expected token is not None, got %s' % str(token)
		user = User.decode(token=token)
		assert not isinstance(user, Exception), 'expected user instance, got Exception %s' % str(user)

	def run(self):
		self.__create_user__()
		self.__token__()
