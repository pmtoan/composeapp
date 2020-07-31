import mysql.connector.pooling


class Pooling:
	"""
	create a pool when connect mysql, which will decrease the time spent in
	request connection, create connection and close connection.
	"""

	def __init__(self, host="172.0.0.1", user="root", password="123456", database="test", pool_name="pool", pool_size=3):
		self.db_config = {
			'host': host,
			'port': 3306,
			'user': user,
			'password': password,
			'database': database,
		}
		self.pool = self.create_pool(pool_name=pool_name, pool_size=int(pool_size))

	def create_pool(self, pool_name="pool", pool_size=3):
		"""
		Create a connection pool, after created, the request of connecting
		MySQL could get a connection from this pool instead of request to
		create a connection.
		"""
		pool = mysql.connector.pooling.MySQLConnectionPool(
			pool_name=pool_name,
			pool_size=pool_size,
			pool_reset_session=True,
			**self.db_config)
		return pool

	def execute(self, sql):
		"""
		Execute & commit a sql.
		"""
		# get connection form connection pool instead of create one.
		conn = self.pool.get_connection()
		cursor = conn.cursor()
		cursor.execute(sql)
		conn.commit()
		cursor.close()
		conn.close()

	def query(self, sql):
		"""
			Execute query & get output.
		"""
		# get connection form connection pool instead of create one.
		conn = self.pool.get_connection()
		cursor = conn.cursor()
		cursor.execute(sql)
		results = cursor.fetchall()
		cursor.close()
		conn.close()

		return results
