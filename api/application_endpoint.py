import os
import web
import json

from services.application.app_service import AppService
from services.git.git_service import GitService
from services.docker.compose_service import ComposeService
from services.log.build_log_service import BuildLogService


class ApplicationEndpoint:
	def __init__(self):
		self.git_service = GitService(local_folder=os.environ['RESOURCES_PATH'])
		self.compose_service = ComposeService(local_folder=os.environ['RESOURCES_PATH'])
		self.build_log_service = BuildLogService(local_folder=os.environ['LOG_PATH'])

		self.app_service = AppService(
			git_service=self.git_service,
			compose_service=self.compose_service,
			build_log_service=self.build_log_service,
		)

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
