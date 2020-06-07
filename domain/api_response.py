import utilities.time


class ApiResponse:
	def __init__(self, ex=None, data=None):
		self.code = ex is None
		self.error = ex
		self.data = data

	def __ser__(self):
		return {
			'time': utilities.time.current_timestamp(),
			'code': self.code,
			'error': self.error,
			'data': self.data
		}

	def	ser(self):
		return self.__ser__()
