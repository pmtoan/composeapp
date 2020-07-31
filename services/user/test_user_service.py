from domain.user import TestUser
from services.user.user_service import UserService
from services.user.user_service import EmailExisted


class TestUserService:
	def __init__(self):
		self.test_user = TestUser()
		self.service = UserService()

	def __create_user__(self):
		self.test_user.run()
		result = self.service.create_user(user=self.test_user.user)
		assert result is None, 'expected result is None, got %s' % str(result)

		result = self.service.create_user(user=self.test_user.user)
		assert result == EmailExisted, 'expected result EmailExisted, got %s' % str(result)

	def run(self):
		self.__create_user__()
