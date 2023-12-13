from flask import request
from flask.views import MethodView
from routes.blueprints import token_mapping_blp as blp
from schemas import GoogleTokensSchemaPost
from controllers.google_tokens import *
from services import save_history
import copy


@blp.route("/google_data/token_mapping")
class GoogleToken(MethodView):
    def get(self):
        request_copy = copy.copy(request)
        return google_tokens_get(request_copy)

    @blp.arguments(GoogleTokensSchemaPost)
    def post(self, body_data):
        return google_tokens_post(dict(body_data))


@blp.after_request
def save_log(response):
    request_data = request.get_json() if request.get_data() else request.args if request.args else None  # SETS THE VARIABLE TO THE DATA OF REQUEST BODY IF THERE IS, OR REQUEST PARAMS IF THERE ARE.
    save_history(request=request_data, request_url=request.url, response=response.get_json(), status=response.status_code)
    return response
