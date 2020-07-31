import uuid


class Unique:
	@staticmethod
	def generate_id():
		return str(uuid.uuid4())[0:6]


class TestUnique:
	def __init__(self):
		self.test_case = {
			'id': ''
		}

	def __test_generate_id__(self):
		self.test_case['id'] = Unique.generate_id()
		assert len(self.test_case['id']) == 6, 'expected id len is 6, but got %d' % len(self.test_case['id'])

	def run(self):
		self.__test_generate_id__()
