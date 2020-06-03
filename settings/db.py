import os
import sqlite3


class Database:
	def __init__(self, path=None):
		self.path = path
		if self.path is None:
			self.path = os.environ['DB_PATH']

		self.conn = None

		self.__connect__()

	def __connect__(self):
		self.conn = sqlite3.connect(self.path)

	# execute a query and commit transaction
	def execute(self, sql):
		cursor = self.conn.cursor()
		cursor.execute(sql)
		self.conn.commit()
		cursor.close()

	def query(self, sql):
		cursor = self.conn.cursor()
		cursor.execute(sql)
		results = cursor.fetchall()
		cursor.close()

		return results

	# migrate database
	def migrate(self):
		with open(os.path.join('settings', 'db.sql'), 'r') as fp:
			queries = fp.read().split(';')
			for query in queries:
				self.execute(query)
