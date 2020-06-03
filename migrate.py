from dotenv import load_dotenv
from settings.db import Database


if __name__ == '__main__':
	load_dotenv(verbose=True)

	db = Database()
	db.migrate()
