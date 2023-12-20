from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import *
from controllers.google_config import *
from utils import save_history

blp = Blueprint('google data', __name__, description='Google DATA related controllers')
"""
configure app routes:
add/edit/delete app+network_user+id json data that contain 1 bucket 
implementation of logic is in controller module
"""


@blp.route("/google_data/data")
class GoogleConfig(MethodView):
    @blp.arguments(GoogleConfigSchemaPost)
    def post(self, body_data):
        return google_config_post(body_data)

    @blp.arguments(GoogleConfigSchemaPut)
    def put(self, body_data):
        return google_config_put(body_data)

    @blp.arguments(GoogleConfigSchemaDelete)
    def delete(self, body_data):
        return google_config_delete(body_data)


@blp.route("/google_data/data/<s>")
class GoogleConfigParams(MethodView):
    def get(self, s):
        return google_config_get(s)


@blp.after_request
def save_log(response):
    request_data = (
        # SETS THE VARIABLE TO THE DATA OF REQUEST BODY IF THERE IS, OR REQUEST PARAMS IF THERE ARE.
        request.get_json()) if request.get_data()\
        else request.args if request.args\
        else request.headers if request.headers \
        else None

    save_history(request=request_data, request_url=request.url, response=response.get_json(), status=response.status_code)
    return response
