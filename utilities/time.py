import datetime

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
TOKEN_EXPIRED_DAYS = 1


class Time:
	@staticmethod
	def current_timestamp():
		return str(datetime.datetime.now().strftime(TIME_FORMAT))

	@staticmethod
	def check_token_expired(timestamp):
		dt = datetime.datetime.strptime(timestamp, TIME_FORMAT)
		return datetime.datetime.now() > dt

	@staticmethod
	def get_token_expired():
		now = datetime.datetime.now()
		expired_day = now + datetime.timedelta(days=TOKEN_EXPIRED_DAYS)
		return str(expired_day.strftime(TIME_FORMAT))
