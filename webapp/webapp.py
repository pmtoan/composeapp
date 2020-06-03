import os

from jinja2 import Environment, FileSystemLoader


class Webapp:
	def __init__(self):
		self.j2_env = Environment(loader=FileSystemLoader(os.path.join('webapp', 'templates')), trim_blocks=True)

	def GET(self, page):
		if (page is None) | (page == '') | (page == 'home'):
			return self.j2_env.get_template('home.html').render(script='home')
