from flask.views import MethodView
from routes.blueprints import skan_blp as blp
from schemas import Oauth2SchemaPost
from controllers.googleapis import oauth2_post


@blp.route("/oauth2.googleapis.com/token")
class Oauth2(MethodView):
    @blp.arguments(Oauth2SchemaPost)
    def post(self, body_data):
        return oauth2_post(dict(body_data))
