import os

from domain.user import User
from settings.db.connection import Connection
from utilities.logger import Logger


class CanNotCreatUser(Exception):
	def __init__(self):
		super(self).__init__('can not create user')


class EmailExisted(Exception):
	def __init__(self):
		super(self).__init__('email existed')


class CanNotGetUser(Exception):
	def __init__(self):
		super(self).__init__('can not get user')


class UserNotFound(Exception):
	def __init__(self):
		super(self).__init__('can not get user')


class UserService:
	def __init__(self, db_pool=None):
		self.pool = None
		self.conn = None

		if db_pool is None:
			Logger.warn('can not get database connection pool from env')
			Logger.info('create a new temporary database connection for this call')
			self.conn = Connection(
				host=os.environ['DB_HOST'],
				user=os.environ['DB_USER'],
				password=os.environ['DB_PWD'],
				database=os.environ['DB_NAME'],
			)
		else:
			self.pool = db_pool

	def __query__(self, sql=None):
		if self.pool is not None:
			results = self.pool.query(sql=sql)
		else:
			results = self.conn.query(sql=sql)

		return results

	def __execute__(self, sql):
		if self.pool is not None:
			status = self.pool.execute(sql=sql)
		else:
			status = self.conn.execute(sql=sql)
		return status

	def __get_user_by_id__(self, user_id=None):
		if user_id is None:
			return None
		sql = '''
			SELECT id, email, password, github_token, created_at, last_access
			FROM users WHERE id = '%s' AND deleted_at IS NULL
		''' % user_id
		results = self.__query__(sql=sql)
		if isinstance(results, Exception):
			return CanNotGetUser
		else:
			for result in results:
				return self.__scan_user__(raw_data=result)
			return UserNotFound

	def __get_user_by_email__(self, email=None):
		if email is None:
			return None
		sql = '''
			SELECT id, email, password, github_token, created_at, last_access
			FROM users WHERE email = '%s' AND deleted_at IS NULL
		''' % email
		results = self.__query__(sql=sql)
		if isinstance(results, Exception):
			return CanNotGetUser
		else:
			for result in results:
				return self.__scan_user__(raw_data=result)
			return UserNotFound

	@staticmethod
	def __scan_user__(raw_data):
		user = User.scan({
			'id': raw_data[0],
			'email': raw_data[1],
			'password': raw_data[2],
			'github': {
				'token': raw_data[3],
			},
			'audit': {
				'created_at': raw_data[4],
				'last_access': raw_data[5],
			},
		})
		return user

	def create_user(self, user=None):
		existed_user = self.get_user(email=user.email)
		if isinstance(existed_user, User):
			return EmailExisted
		if isinstance(existed_user, CanNotGetUser):
			return CanNotCreatUser

		sql = '''
			INSERT INTO users(id, email, password, github_token, created_at, last_access)
			VALUES('%s', '%s', '%s', '%s', '%s', '%s')
		''' % (user.id, user.email, user.password, user.github_token, user.created_at, user.last_access)
		status = self.__execute__(sql=sql)
		if status is not None:
			return CanNotCreatUser
		return status

	def get_user(self, user_id=None, email=None):
		if user_id is not None:
			return self.__get_user_by_id__(user_id=user_id)
		elif email is not None:
			return self.__get_user_by_email__(email=email)
		else:
			return None
