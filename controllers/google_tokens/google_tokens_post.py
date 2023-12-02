from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import GoogleTokensModel


def google_tokens_post(body_data):
    try:
        existing = GoogleTokensModel.query.filter_by(app_id=body_data['app_id'], network_user_id=body_data['network_user_id'], access_token=body_data['access_token']).first()
        if existing:
            db.session.delete(existing)

        data = GoogleTokensModel(**body_data)
        db.session.add(data)
        db.session.commit()

    except SQLAlchemyError:
        abort(400, message="An error occurred while adding token")

    return body_data
