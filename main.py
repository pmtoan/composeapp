import web
import settings.web_urls

from dotenv import load_dotenv

from api.global_endpoint import GlobalEndpoint
from api.application_endpoint import ApplicationEndpoint
from api.build_log_endpoint import BuildLogEndpoint
from api.user_endpoint import UserEndpoint
from webapp.webapp import Webapp

if __name__ == '__main__':
	load_dotenv(verbose=True)

	app = web.application(settings.web_urls.path, globals())
	app.run()
