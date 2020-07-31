from utilities.prototype import *


class Image:
	def __init__(self, attrs=None, short_id=None, tags=None):
		self.attrs = value_or_none(attrs)
		self.id = value_or_none(short_id)
		self.tags = list_items(tags)

	def created_at(self):
		return value_or_none(self.attrs['Created'])
