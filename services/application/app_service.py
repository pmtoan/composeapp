import utilities.time

from settings.db import Database
from domain.application import Application
from domain.build_history import BuildHistory
from domain.git_clone_request import GitCloneRequest
from domain.compose_request import ComposeRequest


class AppService:
	def __init__(self, git_service=None, compose_service=None, build_log_service=None):
		self.database = Database()
		self.git_service = git_service
		self.compose_service = compose_service
		self.build_log_service = build_log_service

	def __get_build_history__(self, app_id=None):
		# query build history
		build_history_query = '''
			SELECT build_id, app_id, built_at, code
			FROM build_histories
			WHERE app_id = '%s'
		''' % app_id
		return self.database.query(build_history_query)

	def __set_last_build__(self, app_id=None):
		sql = '''
			UPDATE applications SET last_build = '%s'
			WHERE id = '%s'
		''' % (utilities.time.current_timestamp(), app_id)
		self.database.execute(sql=sql)

	def __set_build_history__(self, build_history=None):
		sql = '''
			INSERT INTO build_histories(build_id, app_id, built_at, code)
			VALUES('%s', '%s', '%s', %d)
		''' % (build_history.build_id, build_history.app_id, build_history.built_at, build_history.code)

		self.database.execute(sql)

	def __save_build_log__(self, app_id=None, code=None, output=None):
		build_history = BuildHistory(app_id=app_id, code=code)
		build_history.create()
		self.__set_build_history__(build_history=build_history)

		self.build_log_service.save(build_id=build_history.build_id, output=output)

	def create_app(self, app=None):
		# create new application
		# param @app: domain Application instance

		try:
			sql = '''
				INSERT INTO applications(id, name, desc, repository, created_at, last_build)
				VALUES('%s', '%s', '%s', '%s', '%s', '%s')
			''' % (app.id, app.name, app.desc, app.repository, app.created_at, app.last_build)
			self.database.execute(sql)
			return None

		except Exception as e:
			return e

	def get_app(self, app_id=None):
		if app_id is None:
			return None

		app = Application()
		sql = '''
			SELECT id, name, desc, repository, created_at, last_build
			FROM applications
			WHERE id = '%s'
		''' % app_id
		results = self.database.query(sql)

		for result in results:
			app.scan(
				fields=result,
				build_history=self.__get_build_history__(app_id)
			)
			return app

		return None

	def get_apps(self):
		apps = []
		sql = '''
			SELECT id, name, desc, repository, created_at, last_build
			FROM applications
		'''
		results = self.database.query(sql)
		for result in results:
			app = Application()
			app.scan(
				fields=result,
				build_history=self.__get_build_history__(result[0])
			)
			apps.append(app)

		return apps

	def build_app(self, app_id=None):
		app = self.get_app(app_id)
		if app is None:
			return None

		# git clone repo
		clone_request = GitCloneRequest(link=app.repository, folder=app.id)
		return_code, output = self.git_service.clone(clone_request)
		if return_code != 0:
			self.__save_build_log__(app_id=app_id, code=return_code, output=output)
			self.__set_last_build__(app_id=app_id)
			return return_code, output

		compose_request = ComposeRequest(app_id=app_id, compose_file='docker-compose.yml')
		return_code, down_output = self.compose_service.down(compose_request)
		output += down_output
		if return_code != 0:
			self.__save_build_log__(app_id=app_id, code=return_code, output=output)
			self.__set_last_build__(app_id=app_id)
			return return_code, output
		return_code, up_output = self.compose_service.up(compose_request)
		output += up_output
		self.__save_build_log__(app_id=app_id, code=return_code, output=output)
		self.__set_last_build__(app_id=app_id)

		return return_code, output
