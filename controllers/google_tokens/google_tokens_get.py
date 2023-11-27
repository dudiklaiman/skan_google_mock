from flask_smorest import abort
from models import GoogleTokensModel


def google_tokens_get(body_data):
    if 'app_id' in body_data:
        result = GoogleTokensModel.query.filter_by(app_id=body_data['app_id']).first()
        if not result:
            abort(404, message="No matching app_id found")
        return {'access_token': result.access_token}

    elif 'access_token' in body_data:
        result = GoogleTokensModel.query.filter_by(access_token=body_data['access_token']).first()
        if not result:
            abort(404, message="No matching access_token found")
        return {'app_id': result.app_id}

    else:
        abort(400, message="Invalid token_data")
