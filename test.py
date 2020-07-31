from utilities.unique import TestUnique
from services.user.test_user_service import TestUserService

from dotenv import load_dotenv


if __name__ == '__main__':
	load_dotenv(verbose=True)

	test = TestUnique()
	test.run()

	test = TestUserService()
	test.run()
