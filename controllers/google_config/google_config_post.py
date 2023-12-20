from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import GoogleConfigModel
import json
from uuid import uuid4


def google_config_post(body_data):
    """
        method is responsible to add input bucket data to db.
        the assumption is that we need to build path according to given values when only app_id is mandatory,
        for example if we got only app_id and customer_id will be app_id.customer_id and value is customer_id
    """

    # create default dictionary
    init_dict = {"app_id": body_data['app_id'],
                 "network_user_id": body_data['network_user_id'],
                 "customer_id": body_data['network_user_id'],
                 "customer_client": body_data['app_id'],
                 "bucket_id": uuid4().hex[:6],
                 "campaign_id": f"{body_data['network_user_id']}{body_data['app_id']}",
                 "skAdNetworkAttributionCredit": True,
                 "skAdNetworkUserType": "NEW_INSTALLER",
                 "skAdNetworkPostbackSequenceIndex": "0",
                 "skAdNetworkSourceType": "UNAVAILABLE",
                 "skAdNetworkAdEventType": "INTERACTION",
                 "campaign_name": body_data['campaign_name'],
                 "skAdNetworkTotalConversions": body_data['skAdNetworkTotalConversions'],
                 "skAdNetworkInstalls": body_data['skAdNetworkTotalConversions']}

    # edit the init_dict with the user input
    init_dict |= body_data
    tmp_dict = {**init_dict}

    # create list of all paths for example: list[app_id,app_id.network_user_id,....]
    dict_values = list(init_dict.values())
    id_paths = dict_values[:5]
    fix_path = []
    length = 1
    for item in id_paths:
        fix = '.'.join(id_paths[:length])
        fix_path.append(fix)
        length += 1

    # Create a list of config_models that we will add to the db
    index = 1
    config_models = []
    # for every path in fix_path add the value and append to db
    for path in fix_path:
        db_data = GoogleConfigModel.query.filter_by(google_path=path).all()
        # first four paths
        if len(fix_path) > index:
            data = {"google_path": path, "value": json.dumps(id_paths[index])}
            # delete existing item in row if it contains same path and same value
            for item in db_data:
                if item.value == data['value'] or json.loads(item.value) == data["google_path"].split('.')[-1]:
                    db.session.delete(item)
            config_model = GoogleConfigModel(**data)
            config_models.append(config_model)
            index += 1
        # last path (contains bucket)
        else:
            for key in ["app_id", "network_user_id", "customer_id", "customer_client", "bucket_id"]:
                init_dict.pop(key)
            data = {"google_path": path, "value": json.dumps(init_dict)}
            # delete existing item in row if it has same path even if value is not the same
            for item in db_data:
                db.session.delete(item)

            config_model = GoogleConfigModel(**data)
            config_models.append(config_model)
    # after getting list with all the models we need to add it to the db
    try:
        for model in config_models:
            db.session.add(model)
        db.session.commit()
    except SQLAlchemyError:
        abort(500, message="error while insert config data")

    return tmp_dict
