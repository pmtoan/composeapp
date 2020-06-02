import os

from dotenv import load_dotenv
from settings.db import Database
from services.application.app_service import AppService
from services.application.app_composer import AppComposer
from services.git.git_service import GitService
from services.docker.compose_service import ComposeService
from services.log.build_log_service import BuildLogService

if __name__ == '__main__':
	load_dotenv(verbose=True)

	db = Database()
	db.migrate()

	composer = AppComposer()

	git_service = GitService(local_folder=os.environ['RESOURCES_PATH'])
	compose_service = ComposeService(local_folder=os.environ['RESOURCES_PATH'])
	build_log_service = BuildLogService(local_folder=os.environ['LOG_PATH'])

	app_service = AppService(
		database=db,
		git_service=git_service,
		compose_service=compose_service,
		build_log_service=build_log_service,
	)

	app = composer.build_create_app_request(
		name='example go service',
		desc='An example service written in Golang',
		repo_link='https://github.com/pmtoan/example-go-service'
	)
	result = app_service.create_app(app)

	print(app_service.build_app(app_id=app.id))
