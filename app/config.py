from web import database, notfound, internalerror
from jinja2 import Environment, FileSystemLoader
from os.path import dirname, abspath
from sys import argv
from json import loads

__version__ = '0.1'

PATH = abspath(dirname(argv[0]))

DB_DRIVER = 'mysql'
DB_NAME = ''
DB_AUTH = {'u': '', 'p': ''}
DB = database(dbn=DB_DRIVER, db=DB_NAME, user=DB_AUTH['u'], pw=DB_AUTH['p'])


CSS = '/static/css'
IMAGES = '/static/img'
JS = '/static/js'
SESSION = ''


def get_path():
    return PATH


def put_session(session):
    global SESSION
    SESSION = session


def render_not_found():
    render_view = render_template('app/templates/404.jinja2')
    return notfound(render_view)


def render_internal_error():
    render_view = render_template('app/templates/500.jinja2')
    return internalerror(render_view)


def render_template(template_name, **context):
    extensions = context.pop('extensions', [])
    assets = {'CSS': CSS, 'IMAGES': IMAGES, 'JS': JS, 'SESSION': SESSION.data}
    _globals = context.pop('globals', assets)
    template_loader = FileSystemLoader(searchpath=PATH)
    jinja_env = Environment(loader=template_loader, extensions=extensions)
    jinja_env.globals.update(_globals)

    return jinja_env.get_template(template_name).render(context)


def generate_dict_urls():
    file_content = open(PATH + '/app/urls.json').read()
    if file_content:
        try:
            content = loads(file_content)
        except Exception as ex:
            return False
    else:
        return False

    if not content:
        return False
    urls = []
    for bundle, bundle_value in content.items():

        for route, route_value in bundle_value.items():
            name = 'bundles.'+bundle+'.controllers.'+route_value['controller']+'.'+route_value['action']
            urls.append(route)
            urls.append(name)

    return tuple(urls)