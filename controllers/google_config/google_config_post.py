from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError
import json
from db import db
from models import GoogleConfigModel
import json


def google_config_post(body_data):
    init_dict = {"app_id": "", "network_user_id": None, "customer_id": None, "customer_client": None, "bucket_id": None}
    init_dict |= body_data
    dict_values = list(init_dict.values())
    id_paths = dict_values[:5]
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
        db_data = GoogleConfigModel.query.filter_by(google_path=item).all()
        if len(fix_path) > index:
            data = {"google_path": item, "value": json.dumps(id_paths[index])}
            for item in db_data:
                if item.value == data['value'] or json.loads(item.value) == data["google_path"].split('.')[-1]:
                    db.session.delete(item)
            config_model = GoogleConfigModel(**data)
            config_models.append(config_model)
            index += 1
        else:
            if len(fix_path) == 5 and len(dict_values) > 5:
                for key in ["app_id", "network_user_id", "customer_id", "customer_client"]:
                    init_dict.pop(key)
                data = {"google_path": item, "value": json.dumps(init_dict)}
                for item in db_data:
                    db.session.delete(item)
                config_model = GoogleConfigModel(**data)
                config_models.append(config_model)
            else:
                data = {"google_path": item, "value": json.dumps(id_paths[index - 1])}
                for item in db_data:
                    if item.value == data['value'] or json.loads(item.value) == data["google_path"].split('.')[-1]:
                        db.session.delete(item)
                config_model = GoogleConfigModel(**data)
                config_models.append(config_model)
    try:
        for model in config_models:
            db.session.add(model)
        db.session.commit()
    except SQLAlchemyError:
        abort(500, message="error while insert config data")
    return body_data
