import os
import subprocess


class ComposeService:
	def __init__(self, local_folder=None):
		self.local_folder = local_folder
		self.compose_bin = os.path.join('/', 'usr', 'local', 'bin', 'docker-compose')

	def check_env(self):
		return os.path.exists(self.compose_bin)

	def __run__(self, cmd, folder):
		cmd = self.compose_bin + cmd
		sp = subprocess.Popen(cmd, shell=True, cwd=folder, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = sp.communicate()

		return sp.returncode, (out + err).decode('utf-8')

	def up(self, request=None):
		# request is a ComposeRequest instance
		if request is None:
			return 0, ''

		run_folder = os.path.join(self.local_folder, request.app_id)
		if not os.path.exists(run_folder):
			return -1, 'application source not found'

		return self.__run__(request.get_up_cmd(), run_folder)

	def down(self, request=None):
		# request is a ComposeRequest instance
		if request is None:
			return 0, ''

		run_folder = os.path.join(self.local_folder, request.app_id)
		if not os.path.exists(run_folder):
			return -1, 'application source not found'

		return self.__run__(request.get_down_cmd(), run_folder)
