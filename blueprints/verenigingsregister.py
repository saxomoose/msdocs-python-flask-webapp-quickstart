from flask import make_response, request, g
from apiflask import abort, APIBlueprint
from services import databricks_service
from werkzeug.security import check_password_hash
import base64
import os

DQS_API_VERSION_URL = os.getenv('DQS_API_VERSION_URL')
url_prefix_verenigingsregister = f"/api/{DQS_API_VERSION_URL}/verenigingsregister"

blueprint_verenigingsregister = APIBlueprint(name='blueprint_verenigingsregister', import_name=__name__, url_prefix=url_prefix_verenigingsregister)

# Security
@blueprint_verenigingsregister.before_request
def authenticate_verenigingsregister():
   auth_header = request.headers.get('Authorization')
   encoded_credentials = auth_header.split(' ')[1]
   decoded_credentials = base64.b64decode(encoded_credentials).decode('utf-8')
   dqs_client_id, dqs_client_secret = decoded_credentials.split(':', 1)
   if not (check_password_hash(pwhash=os.getenv('DQS_API_CLIENT_SECRET_VERENIGINGSREGISTER'), password=dqs_client_secret)):
      abort(401)
   g.dqs_client = {
      'client_id': dqs_client_id,
      'client_name': 'verenigingsregister'
   }
   
@blueprint_verenigingsregister.before_request
def authorize_verenigingsregister():
   if g.dqs_client['client_id'] != os.getenv('DQS_API_CLIENT_ID_VERENIGINGSREGISTER'):
      abort(403)

# Routing
@blueprint_verenigingsregister.route('/catalog', methods=['GET'])
def catalog():
   return databricks_service.get_catalog()