from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import GoogleTokensModel
from utils import generate_slt


def oauth2_post(body_data):
    """
    logic imp of second request:
    get network_user_id and token and return short_live_token
    :param body_data:
    :return:
    """
    try:
        relevant_data = {'network_user_id': body_data['client_id'], 'long_live_token': body_data['refresh_token']}

        data = GoogleTokensModel.query.filter_by(**relevant_data).all()
        if not data:
            abort(404, message="No matching data found")

        short_live_token = generate_slt(relevant_data['long_live_token'], 10)

        for item in data:
            item.short_live_token = short_live_token
            db.session.add(item)

        db.session.commit()

    except SQLAlchemyError:
        abort(400, message="An error occurred while getting token data")

    return {'access_token': short_live_token}
