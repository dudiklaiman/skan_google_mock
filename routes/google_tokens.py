from flask_smorest import Blueprint
from flask import request
from flask.views import MethodView
from schemas import GoogleTokensSchemaPost
from controllers.google_tokens import *
from utils import save_history
import copy


blp = Blueprint('token mapping', __name__, description='token related controllers')


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
    request_data = (
        # SETS THE VARIABLE TO THE DATA OF REQUEST BODY IF THERE IS, OR REQUEST PARAMS IF THERE ARE.
        request.get_json()) if request.get_data()\
        else request.args if request.args\
        else request.headers if request.headers \
        else None

    save_history(request=request_data, request_url=request.url, response=response.get_json(), status=response.status_code)
    return response
