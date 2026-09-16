'''
Date: 15/09/2026
Description: 
Author: Min Min
'''

import os
from flask import Flask

def create_api(test_config=None):
    # create and configure the api
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists,when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config and pass it
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # simple route
    @app.route('/')
    def hello():
        return 'Hello world'

    return app