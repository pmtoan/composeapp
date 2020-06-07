import web
import json
import utilities.crypto

from domain.api_response import ApiResponse
from domain.user_token import UserToken
from services.user.user_compose import UserCompose
from services.user.user_service import UserService


class UserEndpoint:
	def __init__(self):
		self.user_compose = UserCompose()
		self.user_service = UserService()

		self.token = web.ctx.env.get('HTTP_API_TOKEN')
		self.query = web.input()
		self.data = web.data()

	def __validate_create_user_request__(self):
		user_token = UserToken(token=self.token)
		if user_token.is_admin():
			post_data = json.loads(self.data)
			return self.user_compose.compose_create_user_request(post_data['username'], post_data['password'], 'admin')
		else:
			raise Exception('permission denied')

	def __validate_login_request__(self):
		post_data = json.loads(self.data)
		return self.user_compose.compose_login_user_request(post_data['username'], post_data['password'])

	@staticmethod
	def __get_user_info__(token):
		return utilities.crypto.decode_jwt_token(token=token)

	def __create_user__(self):
		new_user = self.__validate_create_user_request__()
		if isinstance(new_user, Exception):
			return ApiResponse(ex=new_user, data=None)

		result = self.user_service.create_user(user=new_user)
		return ApiResponse(ex=result, data=None)

	def __login_user__(self):
		login_user = self.__validate_login_request__()
		token = self.user_service.login(user=login_user)
		if isinstance(token, Exception):
			return ApiResponse(ex=token, data=None)
		else:
			return ApiResponse(ex=None, data={'token': token})

	def GET(self, action):
		token = web.ctx.env.get('HTTP_API_TOKEN')
		return json.dumps(self.__get_user_info__(token=token))

	def POST(self, action):
		web.header('Access-Control-Allow-Origin', '*')
		if action == '_':
			# create new user
			return json.dumps(self.__create_user__().ser())

		elif action == 'login':
			# user login to get a token key
			return json.dumps(self.__login_user__().ser())
