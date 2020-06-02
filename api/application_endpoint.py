import os
import web
import json

from services.application.app_service import AppService
from services.application.app_composer import AppComposer
from services.git.git_service import GitService
from services.docker.compose_service import ComposeService
from services.log.build_log_service import BuildLogService


class ApplicationEndpoint:
	def __init__(self):
		self.app_compose = AppComposer()
		self.git_service = GitService(local_folder=os.environ['RESOURCES_PATH'])
		self.compose_service = ComposeService(local_folder=os.environ['RESOURCES_PATH'])
		self.build_log_service = BuildLogService(local_folder=os.environ['LOG_PATH'])

		self.app_service = AppService(
			git_service=self.git_service,
			compose_service=self.compose_service,
			build_log_service=self.build_log_service,
		)

	def __validate_create_app_request__(self, data):
		request = json.loads(data)
		return self.app_compose.build_create_app_request(request['name'], request['desc'], request['repo_link'])

	def GET(self, app_id):
		web.header('Access-Control-Allow-Origin', '*')

		if app_id == '_':
			# get all apps
			return json.dumps([])
		else:
			app = self.app_service.get_app(app_id=app_id)
			if app is None:
				return json.dumps({})
			else:
				return json.dumps(repr(app))

	def POST(self, app_id):
		web.header('Access-Control-Allow-Origin', '*')

		if app_id == '_':
			# create app
			app = self.__validate_create_app_request__(web.data())
			result = self.app_service.create_app(app)
			if result is None:
				return json.dumps({'error': ''})
			else:
				return json.dumps({'error': result})
		else:
			# build app
			return_code, output = self.app_service.build_app(app_id=app_id)
			return json.dumps({'code': return_code, 'output': output})
