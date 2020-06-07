import utilities.uuid
import utilities.crypto

ADMIN_ROLE = 'admin'
VIEWER_ROLE = 'viewer'


class User:
	def __init__(self, username=None, password=None, role='viewer'):
		self.id = None
		self.username = username
		self.password = password
		self.role = role

	def __ser__(self):
		return {
			'id': self.id,
			'username': self.username,
			'role': self.role,
		}

	def __str__(self):
		return str(self.__ser__())

	def ser(self):
		return self.__ser__()

	def to_admin(self):
		self.role = 'admin'

	def to_viewer(self):
		self.role = 'viewer'

	def hash_password(self):
		self.password = utilities.crypto.generate_password_hash(self.password)

	def create(self):
		self.id = utilities.uuid.generate_uuid_v4()
		self.password = utilities.crypto.generate_password_hash(self.password)

	def scan(self, fields):
		self.id = fields[0]
		self.username = fields[1]
		self.password = fields[2]
		self.role = fields[3]
