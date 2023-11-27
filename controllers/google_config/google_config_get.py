import json
from models import GoogleConfigModel


def google_config_get(body_data):
    paths = list(body_data.values())
    fix_path = '.'.join(paths)

    if body_data:
        data = GoogleConfigModel.query.filter_by(google_path=fix_path)
    else:
        data = GoogleConfigModel.query.all()
    all_data = []

    for item in data:
        all_data.append({"google_path": item.google_path, "value": json.loads(item.value)})

    return all_data
