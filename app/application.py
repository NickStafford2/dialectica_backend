"""
application.py  
- creates a Flask app instance and registers the database object
"""

from flask import Flask
from flask_cors import CORS

def create_app(app_name='DIALECTICA_API'):  
    app = Flask(app_name)
    app.config.from_object('app.config.BaseConfig')

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


    from app.api import api
    app.register_blueprint(api, url_prefix="/api")


    return app