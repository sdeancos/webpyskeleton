from web import database, notfound, internalerror
from jinja2 import Environment, FileSystemLoader
from os.path import dirname, abspath
from sys import argv

PATH = abspath(dirname(argv[0]))

DBDRIVER   = 'mysql'
DBNAME     = ''
DBUSER     = ''
DBPASSWORD = ''

DB = database(dbn=DBDRIVER, db=DBNAME, user=DBUSER, pw=DBPASSWORD)

CSS     = '/static/css'
IMAGES  = '/static/img'
JS      = '/static/js'
SESSION = ''


def get_path():
    return PATH


def put_session(session):
    global SESSION
    SESSION = session


def render_not_found():
    render_view = render_template('app/templates/404.html')
    return notfound(render_view)


def render_internal_error():
    render_view = render_template('app/templates/500.html')
    return internalerror(render_view)


def render_template(template_name, **context):
    extensions = context.pop('extensions', [])
    assets = {'CSS': CSS,
              'IMAGES': IMAGES,
              'JS': JS,
              'SESSION': SESSION.data}
    globals = context.pop('globals', assets)

    templateLoader = FileSystemLoader(searchpath=PATH)

    jinja_env = Environment(loader=templateLoader,
                            extensions=extensions)

    jinja_env.globals.update(globals)

    return jinja_env.get_template(template_name).render(context)
