from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError
import json
from db import db
from models import GoogleConfigModel


def google_config_post(config_data):
    paths = [config_data['app_id'], config_data['google_account'], config_data['google_campaign_id']]
    values = [item for item in paths]
    values.pop(0)
    length = len(paths) - 1
    fix_path = []
    for item in paths[:]:
        fix = '.'.join(paths)
        fix_path.append(fix)
        paths.pop(length)
        length -= 1
    fix_path.reverse()
    value_keys = ('skan_campaign_id', 'google_campaign_name')
    value_dict = {key: config_data[key] for key in value_keys}
    values.append(value_dict)
    config_models = []
    index = 0
    for item in values:
        data = {"google_path": fix_path[index], "value": json.dumps(item)}
        config_model = GoogleConfigModel(**data)
        config_models.append(config_model)
        index += 1
    try:
        for model in config_models:
            db.session.add(model)
        db.session.commit()
    except SQLAlchemyError:
        abort(500, message="error while insert config data")
    return config_data
