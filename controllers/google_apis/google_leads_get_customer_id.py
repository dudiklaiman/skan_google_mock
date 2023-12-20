from flask_smorest import abort
import json
from models import GoogleConfigModel, GoogleTokensModel


def google_leads_get_customer_id(header_data, version):
    """
    logic imp of second request:
    get network_user_id + app_id and return list of customers in format customers/<id>
    :param header_data:
    :param version:
    :return: all_data
    """
    # check if version is not 15
    if not version == '15':
        abort(400, message=f"wrong version: {version}")

    try:
        token = header_data['Authorization']
        if 'Bearer ' in token:
            token = token.replace('Bearer ', '')

    except KeyError:
        abort(403, message="Token not received")

    token_data = GoogleTokensModel.query.filter_by(short_live_token=token).all()
    if not token_data:
        abort(403, message="Token is invalid.")

    all_data = []

    for item in token_data:
        fix_path = "{}.{}".format(item.app_id, item.network_user_id)
        data = GoogleConfigModel.query.filter_by(google_path=fix_path).first()
        all_data.append(f"customers/{json.loads(data.value)}")

    return all_data
