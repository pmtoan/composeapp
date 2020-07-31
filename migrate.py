import os

from dotenv import load_dotenv
from settings.db.migration import Migration


if __name__ == '__main__':
	load_dotenv(verbose=True)

	db = Migration(sql_path=os.path.join('settings', 'db', 'composeapp.sql'))
	db.run()
