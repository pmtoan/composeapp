import os
import web

from services.log.build_log_service import BuildLogService


class BuildLogEndpoint:
	def __init__(self):
		self.build_log_service = BuildLogService(local_folder=os.environ['LOG_PATH'])

	def GET(self, build_id=None):
		web.header('Access-Control-Allow-Origin', '*')
		return self.build_log_service.load(build_id=build_id)
