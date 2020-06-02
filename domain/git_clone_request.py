class GitCloneRequest:
	def __init__(self, link=None, folder=None):
		self.link = link
		self.folder = folder

	def __ser__(self):
		return {
			'link': self.link,
			'folder': self.folder,
		}

	def __str__(self):
		return str(self.__ser__())

	def __repr__(self):
		return self.__ser__()

	def get_cmd(self):
		return 'git clone %s %s' % (self.link, self.folder)
