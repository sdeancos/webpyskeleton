from web import application, httpserver, debugerror, config, session
from app import config as appconfig
from app.config import generate_dict_urls

PORT = 8000
DEBUG = True
COOKIE = 'webpyskeleton_cookie_session_id'


class MyApplication(application):
    def run(self, port=PORT, *middleware):
        func = self.wsgifunc(*middleware)
        return httpserver.runsimple(func, ('0.0.0.0', port))

if __name__ == "__main__":
    urlpatterns = generate_dict_urls()
    app = MyApplication(urlpatterns, globals(), True)
    config.session_parameters['cookie_name'] = COOKIE
    session = session.Session(app,
                              session.DiskStore('sessions'),
                              initializer={'data': {}})
    appconfig.put_session(session)
    app.notfound = appconfig.render_not_found
    if DEBUG:
        app.internalerror = debugerror
    else:
        app.internalerror = appconfig.render_internal_error
    app.run()
