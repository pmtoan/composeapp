import web
import json

from services.user.user_compose import UserCompose
from services.user.user_service import UserService


class UserEndpoint:
	def __init__(self):
		self.user_compose = UserCompose()
		self.user_service = UserService()

	def __validate_create_user_request__(self, post_data):
		post_data = json.loads(post_data)
		return self.user_compose.compose_create_user_request(post_data['username'], post_data['password'], 'admin')

	def POST(self, action):
		if action == '_':
			# create new user
			user = self.__validate_create_user_request__(web.data())
			result = self.user_service.create_user(user=user)
			if result is None:
				return json.dumps({'error': ''})
			else:
				return json.dumps({'error': str(result)})
