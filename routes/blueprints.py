from flask_smorest import Blueprint


skan_blp = Blueprint('skan', __name__, description='skan related controllers')
google_config_blp = Blueprint('data', __name__, description='Google DATA related controllers')
token_mapping_blp = Blueprint('token_mapping', __name__, description='Google token related controllers')
