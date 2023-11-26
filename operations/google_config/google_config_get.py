from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError
from models import GoogleConfigModel
import json


def google_config_get():
    try:
        data = GoogleConfigModel.query.all()
        all_data = []
        for item in data:
            all_data.append({"google_path": item.google_path, "value": json.loads(item.value)})

    except SQLAlchemyError:
        abort(500, message="An error occurred while getting data")

    return all_data
