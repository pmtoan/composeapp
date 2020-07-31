import utilities.unique
import utilities.time

from domain.build_history import BuildHistory


class Application:
	def __init__(self, name=None, desc=None, repository=None):
		self.id = None
		self.name = name
		self.desc = desc
		self.created_at = ''
		self.last_build = ''
		self.repository = repository
		self.build_history = []

	def __ser__(self):
		app = {
			'id': self.id,
			'name': self.name,
			'desc': self.desc,
			'created_at': self.created_at,
			'last_build': self.last_build,
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
		self.id = utilities.unique.generate_uuid_v4()
		self.created_at = utilities.time.current_timestamp()

	def scan(self, fields=None, build_history=None):
		if fields is None:
			return

		self.id = fields[0]
		self.name = fields[1]
		self.desc = fields[2]
		self.repository = fields[3]
		self.created_at = fields[4]
		self.last_build = fields[5]

		self.__scan_build_history__(build_history)
