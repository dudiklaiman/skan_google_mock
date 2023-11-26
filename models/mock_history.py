from db import db
from sqlalchemy.sql import func


class MockHistoryModel(db.Model):
    __tablename__ = "skan_mock_history"

    id = db.Column(db.Integer, primary_key=True)
    srn = db.Column(db.String, nullable=False)
    request = db.Column(db.String, nullable=False)
    request_url = db.Column(db.String, nullable=False)
    response = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime(timezone=True), server_default=func.now())