from utilities.time import Time


class Logger:
	@staticmethod
	def error(message):
		print('%s | error | %s' % (Time.current_timestamp(), message))

	@staticmethod
	def warn(message):
		print('%s | warn  | %s' % (Time.current_timestamp(), message))

	@staticmethod
	def info(message):
		print('%s | info  | %s' % (Time.current_timestamp(), message))

	@staticmethod
	def exception(e):
		Logger.error(str(e))
