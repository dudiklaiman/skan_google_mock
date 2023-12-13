from flask import request
from flask.views import MethodView
from routes.blueprints import skan_blp as blp
from controllers.googleapis.customers_get import googleapis_customers_get


@blp.route("/googleads.googleapis.com/v15")
class Oauth2(MethodView):
    def get(self):
        header_data = dict(request.headers)
        return googleapis_customers_get(header_data)
