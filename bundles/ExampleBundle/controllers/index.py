from app.config import render_template
from app.config import Flash


class index:
    def GET(self):
        """
            Example Controller WebpySkeleton
        """
        Controller:

        Flash.set('notice', 'Flash message')
        return render_template('bundles/ExampleBundle/views/index.jinja2')
