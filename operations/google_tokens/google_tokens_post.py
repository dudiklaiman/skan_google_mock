from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError
import json
from db import db
from models import GoogleTokensModel


def google_tokens_post(token_data):
    try:
        data = GoogleTokensModel(**token_data)
        db.session.add(data)
        db.session.commit()

    except SQLAlchemyError:
        abort(400, message="An error occurred while adding token")