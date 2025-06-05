from apiflask import APIFlask
import logging
from blueprints.verenigingsregister import blueprint_verenigingsregister

app = APIFlask(__name__)
# if not app.debug:
#     stream_handler = logging.StreamHandler()
#     stream_handler.setLevel(logging.INFO)
#     app.logger.addHandler(stream_handler)

app.register_blueprint(blueprint_verenigingsregister)

if __name__ == '__main__':
   app.run()
