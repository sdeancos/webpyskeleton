from app.config import render_template

class index:
    def GET(self):
        """
            Example Controller WebpySkeleton
        """
        return render_template('bundles/ExampleBundle/views/index.html')
