from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError
import json
from db import db
from models import GoogleConfigModel


def google_config_post(body_data):
    init_dict = {"app_id": "", "google_account": None, "google_campaign_id": None}
    init_dict |= body_data
    dict_values = list(init_dict.values())
    id_paths = dict_values[:3]
    fix_path = []
    length = 1
    for item in id_paths:
        if not item:
            break
        fix = '.'.join(id_paths[:length])
        fix_path.append(fix)
        length += 1
    index = 1
    config_models = []
    for item in fix_path:
        if len(fix_path) > index:
            data = {"google_path": item, "value": json.dumps(id_paths[index])}
            config_model = GoogleConfigModel(**data)
            config_models.append(config_model)
            index += 1
        else:
            if len(fix_path) == 3 and len(dict_values) > 3:
                for key in ["app_id", "google_account", "google_campaign_id"]:
                    init_dict.pop(key)
                data = {"google_path": item, "value": json.dumps(init_dict)}
                config_model = GoogleConfigModel(**data)
                config_models.append(config_model)
            else:
                data = {"google_path": item, "value": json.dumps(id_paths[index - 1])}
                config_model = GoogleConfigModel(**data)
                config_models.append(config_model)

    try:
        for model in config_models:
            db.session.add(model)
        db.session.commit()
    except SQLAlchemyError:
        abort(500, message="error while insert config data")

    return body_data
