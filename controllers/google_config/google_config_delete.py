from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import GoogleConfigModel


def google_config_delete(body_data):
    paths = [body_data['app_id'], body_data['google_account'], body_data['google_campaign_id']]
    length = len(paths) - 1
    fix_path = []
    for _ in paths[:]:
        fix = '.'.join(paths)
        fix_path.append(fix)
        paths.pop(length)
        length -= 1
    fix_path.reverse()
    try:
        for path in fix_path:
            config_models = GoogleConfigModel.query.filter_by(google_path=path).all()
            if config_models:
                for config_model in config_models:
                    db.session.delete(config_model)
                    db.session.commit()
            else:
                abort(404, message=f"Config data not found for path: {path}")
    except SQLAlchemyError:
        abort(500, message="Error while deleting config data.")

    return {"status": "Success", "message": "Config data deleted successfully"}
