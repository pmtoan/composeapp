import web


class GlobalEndpoint:
	def GET(self, path):
		if path == 'favicon.ico':
			web.seeother('/static/images/logo.png')

		elif (path is None) | (path == ''):
			web.seeother('/app/home')
