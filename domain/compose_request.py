class ComposeRequest:
	def __init__(self, app_id=None, compose_file=None, parameters=None):
		self.app_id = app_id
		self.compose_file = compose_file
		self.parameters = parameters

	def get_up_cmd(self):
		return ' -f %s up -d' % self.compose_file

	def get_down_cmd(self):
		return ' -f %s down' % self.compose_file
