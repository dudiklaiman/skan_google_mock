from db import db
from sqlalchemy.sql import func


class GoogleConfigModel(db.Model):
    __tablename__ = "skan_mock_google_config"

    id = db.Column(db.Integer, primary_key=True)
    google_path = db.Column(db.String, nullable=False)
    value = db.Column(db.String, nullable=False)
    last_update = db.Column(db.DateTime(timezone=True), onupdate=func.now())
