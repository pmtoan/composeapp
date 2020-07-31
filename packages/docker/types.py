from utilities.prototype import *


class BuildDockerImageOption:
	def __init__(self, name=None, version=None, path=None):
		self.name = value_or_none(name)
		self.version = value_or_none(version)
		self.path = value_or_none(path)

	def to_tag(self):
		return self.name + ':' + self.version
