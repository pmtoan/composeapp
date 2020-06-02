import os
import shutil
import subprocess


class GitService:
	def __init__(self, local_folder=None):
		self.local_folder = local_folder

		self.__init_env__()

	def __init_env__(self):
		if not os.path.exists(self.local_folder):
			os.system('mkdir -p %s' % self.local_folder)

	def __run__(self, cmd):
		sp = subprocess.Popen(cmd, shell=True, cwd=self.local_folder, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = sp.communicate()

		return sp.returncode, (out + err).decode('utf-8')

	def clone(self, request=None):
		if request is None:
			return 0, ''

		expected_path = os.path.join(self.local_folder, request.folder)
		if os.path.exists(expected_path):
			shutil.rmtree(expected_path)

		return self.__run__(request.get_cmd())
