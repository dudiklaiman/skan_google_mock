from db import db
from sqlalchemy.sql import func


class GoogleTokensModel(db.Model):
    __tablename__ = "skan_mock_google_tokens"

    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.String, nullable=False)
    network_user_id = db.Column(db.String, nullable=False)
    long_live_token = db.Column(db.String, nullable=False)
    short_live_token = db.Column(db.String, nullable=True)
    last_update = db.Column(db.DateTime(timezone=True), default=func.now(), onupdate=func.now())
    