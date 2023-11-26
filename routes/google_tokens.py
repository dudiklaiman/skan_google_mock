from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import GoogleTokenSchema
from operations.google_tokens import google_tokens_post


blp = Blueprint('token_mapping', __name__, description='Google token related operations')


@blp.route("/google_data/token_mapping")
class GoogleToken(MethodView):
    @staticmethod
    def get():
        pass

    @staticmethod
    @blp.arguments(GoogleTokenSchema)
    def post(token_data):
        return google_tokens_post(token_data)

