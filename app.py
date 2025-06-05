import os

from flask import Flask, request, make_response, Blueprint
from werkzeug.security import check_password_hash
import logging
import base64
from  urllib.parse import urlparse
from blueprints.verenigingsregister import blueprint_verenigingsregister

app = Flask(__name__)
# if not app.debug:
#     stream_handler = logging.StreamHandler()
#     stream_handler.setLevel(logging.INFO)
#     app.logger.addHandler(stream_handler)

app.register_blueprint(blueprint_verenigingsregister)

if __name__ == '__main__':
   app.run()
