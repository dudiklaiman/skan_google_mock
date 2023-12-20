import json
from db import db
from models import GoogleConfigModel


def google_config_put(body_data):
    keys = ("app_id", "network_user_id", "customer_id", "customer_client", "campaign_id")
    my_dict = {key: body_data[key] for key in keys}
    paths = list(my_dict.values())
    fix_path = '.'.join(paths)
    data = GoogleConfigModel.query.filter_by(google_path=fix_path).first()
    for key in keys:
        body_data.pop(key)
    old_value = json.loads(data.value)
    if isinstance(old_value, dict):
        old_value |= body_data
    else:
        old_value = body_data
    data.value = json.dumps(old_value)
    db.session.add(data)
    db.session.commit()

    return body_data
