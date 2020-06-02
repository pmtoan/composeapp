import web


class Root:
	def GET(self, path):
		if path == 'favicon.ico':
			web.seeother('/static/images/logo.png')
