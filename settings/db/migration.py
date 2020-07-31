import os
import mysql.connector


class Migration:
	def __init__(self, sql_path=None):
		self.sql_path = sql_path
		self.conn = None
		self.queries = []

	def __connect__(self):
		try:
			self.conn = mysql.connector.connect(
				host=os.environ['DB_HOST'],
				user=os.environ['DB_USER'],
				password=os.environ['DB_PWD'],
			)
		except Exception as e:
			raise e

	def __read_queries__(self):
		try:
			with open(self.sql_path, 'r') as fp:
				self.queries = fp.read().split(';')
		except Exception as e:
			raise e

	def run(self):
		self.__connect__()
		self.__read_queries__()
		cursor = self.conn.cursor()
		for query in self.queries:
			cursor.execute(query)
			self.conn.commit()
		cursor.close()
		self.conn.close()
