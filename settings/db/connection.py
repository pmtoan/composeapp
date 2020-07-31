import mysql.connector

from utilities.logger import Logger


class Connection:
	def __init__(self, host="172.0.0.1", user="root", password="123456", database="test"):
		self.host = host
		self.user = user
		self.password = password
		self.database = database
		try:
			self.conn = mysql.connector.connect(
				host=self.host,
				user=self.user,
				password=self.password,
				database=self.database
			)
		except Exception as e:
			Logger.exception(e)

	def query(self, sql=None):
		"""
		Execute a query and return data
		:param sql: SQL query string
		:return: array of tupples
		"""
		try:
			cursor = self.conn.cursor()
			cursor.execute(sql)
			results = cursor.fetchall()
			cursor.close()
			return results
		except Exception as e:
			Logger.exception(e)
			return e

	def execute(self, sql=None):
		"""
		Execute a query and commit conn after
		:param sql: query string
		:return: None or Exception
		"""
		try:
			cursor = self.conn.cursor()
			cursor.execute(sql)
			cursor.close()
			self.conn.commit()
			return None
		except Exception as e:
			Logger.exception(e)
			return e
