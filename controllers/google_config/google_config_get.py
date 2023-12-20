import json
from models import GoogleConfigModel


def google_config_get(s):
    """
    will return value according to given path.
    path can contain between 1 param(app_id) to all params(app_id+network_user_id+customer_id+customer_client+bucket_id)
    """

    if not s == "all":
        data = GoogleConfigModel.query.filter_by(google_path=s)
    else:
        data = GoogleConfigModel.query.all()
    all_data = [{"google_path": item.google_path, "value": json.loads(item.value)} for item in data]

    return all_data
