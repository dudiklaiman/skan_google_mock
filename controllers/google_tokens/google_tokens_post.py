from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import GoogleTokensModel, GoogleConfigModel


def google_tokens_post(body_data):
    try:
        existing = GoogleTokensModel.query.filter_by(**body_data).first()
        if existing:
            db.session.delete(existing)

        check = GoogleConfigModel.query.filter_by(google_path=f"{body_data['app_id']}.{body_data['network_user_id']}").first()
        if not check:
            abort(400, message="app or user doesn't exist")

        data = GoogleTokensModel(**body_data)
        db.session.add(data)
        db.session.commit()

    except SQLAlchemyError:
        abort(500, message="An error occurred while adding token")

    return body_data
