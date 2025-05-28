import os

from flask import Flask
import databricks_service
import logging


app = Flask(__name__)
app.config['DEBUG'] = True
if not app.debug:
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    app.logger.addHandler(stream_handler)

@app.route('/catalog')
def catalog():
   return databricks_service.get_catalog()

if __name__ == '__main__':
   app.run()
