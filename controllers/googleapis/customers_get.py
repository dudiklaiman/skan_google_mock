from flask_smorest import abort
from models import GoogleTokensModel
from services import is_valid_dict


def googleapis_customers_get(header_data):
    data = GoogleTokensModel.query.filter_by(access_token=header_data['Authorization']).all()
