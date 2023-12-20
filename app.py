from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from db import db
from routes.google_config import blp as google_config_blp
from routes.google_tokens import blp as google_tokens_blp
from routes.google_apis import blp as google_apis_blp


def create_app():
    """
    before running app run commands:
    Flask db init
    Flask db migrate
    Flask db upgrade
    Flask run
    service(and db) and swagger definition and initiation
    :return:
    """
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "SKAN google mock"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.1.0"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.10.0/"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost:5432/skan_google_mock"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    # migrate = Migrate(app, db)
    Migrate(app, db)

    api = Api(app)
    api.register_blueprint(google_apis_blp)
    api.register_blueprint(google_tokens_blp)
    api.register_blueprint(google_config_blp)

    return app
