from services.git.git_service import GitService
from domain.git_clone_request import GitCloneRequest


class TestGitService:
	def __init__(self):
		self.service = GitService(local_folder='data')

	def __1_clone__(self):
		request = GitCloneRequest(
			link='https://github.com/pmtoan/example-go-service',
			folder='example-go-service'
		)

		code, output = self.service.clone(request)
		assert code == 0, 'expected exit code = 0, but got %d' % code

		request = GitCloneRequest(
			link='https://ithub.com/pmtoan/example-go-service',
			folder='example-go-service'
		)

		code, output = self.service.clone(request)
		assert code != 0, 'expected exit code != 0, but got %d' % code

	def run(self):
		self.__1_clone__()
