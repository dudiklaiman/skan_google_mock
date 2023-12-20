from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from controllers.google_apis import *
from schemas import Oauth2SchemaPost
from utils import save_history


blp = Blueprint('google', __name__, description='google MOCK related controllers')
""" 
request - response routes
"""


@blp.route("/oauth2.googleapis.com/token")
class Oauth2(MethodView):
    @blp.arguments(Oauth2SchemaPost)
    def post(self, body_data):
        return oauth2_post(dict(body_data))


@blp.route("/googleads.googleapis.com/<version>/customers")
class GoogleLeads(MethodView):
    def get(self, version):
        header_data = dict(request.headers)
        return google_leads_get_customer_id(header_data, version)


@blp.route("/googleads.googleapis.com/<version>/customers/<id>/googleAds")
class GoogleLeadsId(MethodView):
    def post(self, version, id):
        req_data = dict(request.headers)
        return google_leads_get_customer_client(req_data, version, id)


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
