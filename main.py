from settings.db import Database


if __name__ == '__main__':
	db = Database()
	db.migrate()
