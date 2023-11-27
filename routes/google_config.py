from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import *
from controllers.google_config import *


blp = Blueprint('data', __name__, description='Google DATA related controllers')


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
