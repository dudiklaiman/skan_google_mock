from db import db
from sqlalchemy.sql import func


class GoogleTokensModel(db.Model):
    __tablename__ = "skan_mock_google_tokens"

    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.String, nullable=False)
    network_user_id = db.Column(db.String, nullable=False)
    access_token = db.Column(db.String, nullable=False)
    last_update = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    