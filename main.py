from web import application, httpserver, debugerror, config, session
from app import config as appconfig, urls

PORT   = 8000
DEBUG  = True
COOKIE = 'webpyskeleton_cookie_session_id'

class MyApplication(application):
    def run(self, port=PORT, *middleware):
        func = self.wsgifunc(*middleware)
        return httpserver.runsimple(func, ('0.0.0.0', port))

if __name__ == "__main__":
    app = MyApplication(urls.urlpatterns, globals(), True)
    if DEBUG:
        app.internalerror = debugerror
    config.session_parameters['cookie_name'] = COOKIE
    session = session.Session(app,
                              session.DiskStore('sessions'),
                              initializer={'data': {}})
    appconfig.put_session(session)
    app.notfound = appconfig.render_notfound
    app.internalerror = appconfig.render_internalerror
    app.run()
