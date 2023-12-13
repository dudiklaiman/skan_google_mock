from flask import request
from flask.views import MethodView
from routes.blueprints import google_config_blp as blp
from schemas import *
from controllers.google_config import *
from services import save_history


@blp.route("/google_data/data")
class GoogleConfig(MethodView):
    @blp.arguments(GoogleConfigSchemaGet)
    def get(self, body_data):
        return google_config_get(body_data)

    @blp.arguments(GoogleConfigSchemaPost)
    def post(self, body_data):
        return google_config_post(body_data)

    @blp.arguments(GoogleConfigSchemaPut)
    def put(self, body_data):
        return google_config_put(body_data)

    @blp.arguments(GoogleConfigSchemaDelete)
    def delete(self, body_data):
        return google_config_delete(body_data)


@blp.after_request
def save_log(response):
    request_data = request.get_json() if request.get_data() else request.args if request.args else None  # SETS THE VARIABLE TO THE DATA OF REQUEST BODY IF THERE IS, OR REQUEST PARAMS IF THERE ARE.
    save_history(request=request_data, request_url=request.url, response=response.get_json(), status=response.status_code)
    return response
