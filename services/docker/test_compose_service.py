from services.docker.compose_service import ComposeService


class TestComposeService:
	def __init__(self):
		self.service = ComposeService()

	def __1_check_env__(self):
		assert self.service.check_env(), 'expected check env return True, but got False'

	def run(self):
		self.__1_check_env__()
