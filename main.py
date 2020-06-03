import web
import settings.api_urls

from dotenv import load_dotenv

from api.root import Root
from api.application_endpoint import ApplicationEndpoint
from api.build_log_endpoint import BuildLogEndpoint

if __name__ == '__main__':
	load_dotenv(verbose=True)

	app = web.application(settings.api_urls.path, globals())
	app.run()
