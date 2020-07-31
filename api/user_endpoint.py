import web
import json

from domain.user import User
from domain.http import ResponseData
from domain.http import ResponseNotFound
from domain.http import HttpCreated
from domain.http import HttpFound
from domain.http import HttpBadRequest
from domain.http import HttpInternalError
from services.user.user_service import UserService
from services.user.user_service import EmailExisted
from services.user.user_service import CanNotCreatUser
from utilities.logger import Logger


class UserEndpoint:
	def __init__(self):
		self.user_service = UserService()
		self.token = web.ctx.env.get('HTTP_MYTOKEN')
		self.query = web.input()
		self.data = web.data()

		web.header('Access-Control-Allow-Origin', '*')

	def __create_user__(self):
		try:
			raw_data = json.loads(self.data)
			user = User(email=raw_data['email'], password=raw_data['password'])
			user.create()
			result = self.user_service.create_user(user=user)
			if result is None:
				raise HttpCreated(data=ResponseData(ex=None, data={'id': user.id, 'email': user.email}))
			elif isinstance(result, EmailExisted):
				raise HttpFound(data=ResponseData(ex=result, data=None))
			else:
				raise HttpInternalError(data=ResponseData(ex=result, data=None))

		except Exception as e:
			Logger.exception(e)
			raise HttpBadRequest(data=ResponseData(ex=e, data=None))

	def POST(self, endpoint):
		if endpoint == 'create':
			# create new user
			self.__create_user__()

		else:
			raise ResponseNotFound
