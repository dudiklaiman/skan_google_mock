from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from services.services import generate_slt
from models import GoogleTokensModel


def oauth2_post(body_data):
    try:
        relevant_data = {'network_user_id': body_data['client_id'], 'access_token': body_data['refresh_token']}

        check = GoogleTokensModel.query.filter_by(**relevant_data).first()
        if not check:
            abort(404, message="No matching key found")

        short_live_token = generate_slt(relevant_data['access_token'], 10)
        relevant_data['access_token'] = short_live_token
        relevant_data['app_id'] = check.app_id

        data = GoogleTokensModel(**relevant_data)
        db.session.add(data)
        db.session.commit()

    except SQLAlchemyError:
        abort(400, message="An error occurred while getting token")

    return {'access_token': short_live_token}
