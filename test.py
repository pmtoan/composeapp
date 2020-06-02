from settings.db import Database
from services.application.test_app_service import TestAppService
from services.git.test_git_service import TestGitService
from services.docker.test_compose_service import TestComposeService


if __name__ == '__main__':
	db = Database()
	db.migrate()

	test_app_service = TestAppService(database=db)
	test_app_service.run()

	test_git_service = TestGitService()
	test_git_service.run()

	test_compose_service = TestComposeService()
	test_compose_service.run()
