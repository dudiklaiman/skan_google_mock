from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import GoogleConfigSchema
from operations.google_config import google_config_get, google_config_post


blp = Blueprint('google_data', __name__, description='Google DATA related operations')


@blp.route("/google_data/data")
class GoogleConfig(MethodView):
    @staticmethod
    def get():
        return google_config_get()

    @staticmethod
    @blp.arguments(GoogleConfigSchema)
    def post(config_data):
        return google_config_post(config_data)

    @staticmethod
    def patch():
        pass

    @staticmethod
    def delete():
        pass
