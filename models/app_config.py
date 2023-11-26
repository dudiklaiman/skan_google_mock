from db import db
from sqlalchemy.sql import func


class AppConfigModel(db.Model):
    __tablename__ = "skan_mock_app_config"

    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.String, nullable=False)
    srn = db.Column(db.String, nullable=False)
    app_configuration = db.Column(db.JSON, nullable=False)
    last_update = db.Column(db.DateTime(timezone=True), onupdate=func.now())
