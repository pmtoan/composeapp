import web
import json
import utilities.crypto

from services.user.user_compose import UserCompose
from services.user.user_service import UserService


class UserEndpoint:
	def __init__(self):
		self.user_compose = UserCompose()
		self.user_service = UserService()

	def __validate_create_user_request__(self, post_data):
		post_data = json.loads(post_data)
		return self.user_compose.compose_create_user_request(post_data['username'], post_data['password'], 'admin')

	def __validate_login_request__(self, post_data):
		post_data = json.loads(post_data)
		return self.user_compose.compose_create_user_request(post_data['username'], post_data['password'], 'admin')

	@staticmethod
	def __get_user_info__(token):
		return utilities.crypto.decode_jwt_token(token=token)

	def GET(self, action):
		token = web.ctx.env.get('HTTP_API_TOKEN')
		return json.dumps(self.__get_user_info__(token=token))

	def POST(self, action):
		web.header('Access-Control-Allow-Origin', '*')
		if action == '_':
			# create new user
			user = self.__validate_create_user_request__(web.data())
			result = self.user_service.create_user(user=user)
			if result is None:
				return json.dumps({'error': ''})
			else:
				return json.dumps({'error': str(result)})

		elif action == 'login':
			# user login to get a token key
			user = self.__validate_login_request__(web.data())
			token = self.user_service.login(user=user)
			if isinstance(token, str):
				return json.dumps({'error': '', 'token': token})
			else:
				return json.dumps({'error': str(token), 'token': ''})
