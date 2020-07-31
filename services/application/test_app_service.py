import os
import utilities.unique

from services.application.app_service import AppService
from services.application.app_composer import AppComposer
from services.git.git_service import GitService
from services.docker.compose_service import ComposeService
from services.log.build_log_service import BuildLogService


class TestAppService:
	def __init__(self, database=None):
		self.database = database
		self.git_service = GitService(local_folder=os.path.join('data', 'resources'))
		self.compose_service = ComposeService(local_folder=os.path.join('data', 'resources'))
		self.build_log_service = BuildLogService(local_folder=os.path.join('data', 'log', 'build_history'))

		self.service = AppService(
			database=database,
			git_service=self.git_service,
			compose_service=self.compose_service,
			build_log_service=self.build_log_service
		)
		self.composer = AppComposer()

		self.app = None

	def __1_create_app__(self):
		self.app = self.composer.build_create_app_request(
			name='example go service',
			desc='An example service written in Golang',
			repo_link='https://github.com/pmtoan/example-go-service'
		)
		result = self.service.create_app(self.app)

		assert result is None, 'expected result None, but got result: %s' % str(result)

	def __2_get_app__(self):
		app = self.service.get_app(app_id=self.app.id)
		assert app is not None, 'expected app not None, but got None'
		assert app.id == self.app.id, 'expected app id is %s, but got %s' % (self.app.id, app.id)
		assert app.name == self.app.name, 'expected app name is %s, but got %s' % (self.app.name, app.name)
		assert app.desc == self.app.desc, 'expected app desc is %s, but got %s' % (self.app.desc, app.desc)
		assert app.repository == self.app.repository, 'expected app repository is %s, but got %s' % (self.app.repository, app.repository)
		assert app.created_at == self.app.created_at, 'expected app created at is %s, but got %s' % (self.app.created_at, app.created_at)
		assert app.updated_at == self.app.updated_at, 'expected app updated at is %s, but got %s' % (self.app.updated_at, app.updated_at)
		assert app.deleted_at == self.app.deleted_at, 'expected app deleted at is %s, but got %s' % (self.app.deleted_at, app.deleted_at)
		assert len(app.build_history) == 0, 'expected build history len = 0, but got %d' % len(app.build_history)

		app = self.service.get_app(app_id=utilities.unique.generate_uuid_v4())
		assert app is None, 'expected app is None, but got not None'

	def __3_build_app__(self):
		print(self.service.build_app(app_id=self.app.id))
		app = self.service.get_app(app_id=self.app.id)

		assert app is not None, 'expected app not None, but got None'
		assert app.id == self.app.id, 'expected app id is %s, but got %s' % (self.app.id, app.id)
		assert app.name == self.app.name, 'expected app name is %s, but got %s' % (self.app.name, app.name)
		assert app.desc == self.app.desc, 'expected app desc is %s, but got %s' % (self.app.desc, app.desc)
		assert app.repository == self.app.repository, 'expected app repository is %s, but got %s' % (self.app.repository, app.repository)
		assert app.created_at == self.app.created_at, 'expected app created at is %s, but got %s' % (self.app.created_at, app.created_at)
		assert app.updated_at == self.app.updated_at, 'expected app updated at is %s, but got %s' % (self.app.updated_at, app.updated_at)
		assert app.deleted_at == self.app.deleted_at, 'expected app deleted at is %s, but got %s' % (self.app.deleted_at, app.deleted_at)
		assert len(app.build_history) == 1, 'expected build history len = 1, but got %d' % len(app.build_history)

	def run(self):
		self.__1_create_app__()
		self.__2_get_app__()
		self.__3_build_app__()
