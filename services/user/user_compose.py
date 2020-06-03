from domain.user import User


class UserCompose:
	@staticmethod
	def compose_create_user_request(username, password, role):
		user = User(username=username, password=password, role=role)
		user.create()
		return user
