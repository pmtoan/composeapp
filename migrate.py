from dotenv import load_dotenv
from settings.db import Database
from services.user.user_compose import UserCompose
from services.user.user_service import UserService


if __name__ == '__main__':
	load_dotenv(verbose=True)

	db = Database()
	db.migrate()

	user = UserCompose.compose_create_user_request(username='admin', password='admin', role='admin')
	user_service = UserService()
	user_service.create_user(user=user)
