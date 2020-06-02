import os


class BuildLogService:
	def __init__(self, local_folder):
		self.local_folder = os.path.join(local_folder, 'build_history')

		self.__init_env__()

	def __init_env__(self):
		if not os.path.exists(self.local_folder):
			os.system('mkdir -p %s' % self.local_folder)

	def save(self, build_id=None, output=None):
		# request is a SaveBuildLogRequest instance
		log_path = os.path.join(self.local_folder, build_id)
		with open(log_path, 'w', encoding='utf-8') as fp:
			fp.write(output)

	def load(self, build_id):
		log_path = os.path.join(self.local_folder, build_id)
		if not os.path.exists(log_path):
			return ''

		with open(log_path, 'r', encoding='utf-8') as fp:
			return fp.read()
