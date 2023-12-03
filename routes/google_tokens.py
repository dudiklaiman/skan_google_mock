from flask import request
from flask.views import MethodView
from routes.blueprints import token_mapping_blp as blp
from schemas import GoogleTokensSchemaPost
from controllers.google_tokens import *


@blp.route("/google_data/token_mapping")
class GoogleToken(MethodView):
    def get(self):
        params_data = dict(request.args)
        return google_tokens_get(params_data)

    @blp.arguments(GoogleTokensSchemaPost)
    def post(self, body_data):
        return google_tokens_post(dict(body_data))
