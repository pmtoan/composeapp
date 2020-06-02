import utilities.uuid
import utilities.time

from domain.build_history import BuildHistory


class Application:
	def __init__(self, name=None, desc=None, repository=None):
		self.id = None
		self.name = name
		self.desc = desc
		self.created_at = None
		self.updated_at = None
		self.deleted_at = None
		self.repository = repository
		self.build_history = []

	def __ser__(self):
		app = {
			'name': self.name,
			'desc': self.desc,
			'created_at': self.created_at,
			'updated_at': self.updated_at,
			'deleted_at': self.deleted_at,
			'repository': self.repository,
			'build_history': []
		}
		for bh in self.build_history:
			app['build_history'].append(bh.ser())

		return app

	def __str__(self):
		return str(self.__ser__())

	def __repr__(self):
		return self.__ser__()

	def __scan_build_history__(self, rows):
		if rows is None:
			return

		for row in rows:
			build_history = BuildHistory()
			build_history.scan(row)
			self.build_history.append(build_history)

	def ser(self):
		return self.__ser__()

	def create(self):
		self.id = utilities.uuid.generate_uuid_v4()
		self.created_at = self.updated_at = utilities.time.current_timestamp()

	def scan(self, fields=None, build_history=None):
		if fields is None:
			return

		self.id = fields[0]
		self.name = fields[1]
		self.desc = fields[2]
		self.repository = fields[3]
		self.created_at = fields[4]
		self.updated_at = fields[5]
		self.deleted_at = fields[6]
		if self.deleted_at == 'None':
			self.deleted_at = None

		self.__scan_build_history__(build_history)
