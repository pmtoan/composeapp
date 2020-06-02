from domain.application import Application


class AppComposer:
	def __init__(self):
		pass

	@staticmethod
	def build_create_app_request(name=None, desc=None, repo_link=None):
		app = Application(name=name, desc=desc, repository=repo_link)
		app.create()

		return app
