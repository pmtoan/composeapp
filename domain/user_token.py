import utilities.crypto

from domain.user import ADMIN_ROLE
from domain.user import VIEWER_ROLE
from domain.user import User


class UserToken:
	def __init__(self, token=None):
		self.token = token
		self.user = None
		self.exception = None

		self.__parse__()

	def __parse__(self):
		self.user = User()
		try:
			raw_user = utilities.crypto.decode_jwt_token(token=self.token)
			self.user.id = raw_user['id']
			self.user.username = raw_user['username']
			self.user.role = raw_user['role']

		except Exception as e:
			self.exception = e

	def is_admin(self):
		return self.user.role == ADMIN_ROLE

	def is_viewer(self):
		return self.user.role == VIEWER_ROLE
