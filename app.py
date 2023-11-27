from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from routes.google_config import blp as google_config_bl
from routes.google_tokens import blp as google_tokens_bl
from db import db


def create_app():
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
    migrate = Migrate(app, db)

    api = Api(app)
    api.register_blueprint(google_config_bl)
    api.register_blueprint(google_tokens_bl)

    return app
