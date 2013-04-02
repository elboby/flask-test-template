from flask import Flask
from blank import blank as blank_bp

def create_app(template_folder='templates'):
    app = Flask(__name__, 
                template_folder=template_folder,)
    app.debug = True
    app.register_blueprint(blank_bp)
    return app
