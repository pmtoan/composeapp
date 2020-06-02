import utilities.uuid
import utilities.time


class BuildHistory:
	def __init__(self, build_id=None, app_id=None, built_at=None, code=0):
		self.build_id = build_id
		self.app_id = app_id
		self.built_at = built_at
		self.code = code

	def __ser__(self):
		return {
			'build_id': self.build_id,
			'app_id': self.app_id,
			'built_at': self.built_at,
			'code': self.code,
		}

	def __str__(self):
		return str(self.__ser__())

	def __repr__(self):
		return self.__ser__()

	def create(self):
		self.build_id = utilities.uuid.generate_uuid_v4()
		self.built_at = utilities.time.current_timestamp()

	def scan(self, fields):
		self.build_id = fields[0]
		self.app_id = fields[1]
		self.built_at = fields[2]
		self.code = fields[3]

	def ser(self):
		return self.__ser__()
