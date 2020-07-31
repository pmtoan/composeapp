import web
import json

from utilities.time import Time


HTTP_CONTENT_TYPE_JSON = {'Content-Type': 'application/json'}


class ResponseData:
    def __init__(self, ex=None, data=None):
        self.error = ex
        self.data = data

    def __ser__(self):
        return {
            'time': Time.current_timestamp(),
            'error': self.error,
            'data': self.data
        }

    def ser(self):
        return self.__ser__()

    def json(self):
        return json.dumps(self.ser())


class ResponseNotFound(web.webapi.NotFound):
    def __init__(self):
        web.webapi.NotFound(json.dumps({'message': 'not found'}))


class HttpCreated(web.webapi.Created):
    def __init__(self, data=None):
        web.webapi.Created(self, headers=HTTP_CONTENT_TYPE_JSON, data=data.json())


class HttpUnauthorized(web.webapi.Unauthorized):
    def __init__(self, data=None):
        web.webapi.Created(self, headers=HTTP_CONTENT_TYPE_JSON, data=data.json())


class HttpFound(web.webapi.Found):
    def __init__(self, data=None):
        web.webapi.Created(self, headers=HTTP_CONTENT_TYPE_JSON, data=data.json())


class HttpBadRequest(web.webapi.BadRequest):
    def __init__(self, data=None):
        web.webapi.Created(self, headers=HTTP_CONTENT_TYPE_JSON, data=data.json())


class HttpInternalError(web.webapi.InternalError):
    def __init__(self, data=None):
        web.webapi.Created(self, headers=HTTP_CONTENT_TYPE_JSON, data=data.json())
