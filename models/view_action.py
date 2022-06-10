from dataclasses import dataclass

from ..extensions import db

@dataclass
class ViewAction(db.Model):
    _userId : str
    _sessionId : str
    _time : str
    _viewedId : str

    __tablename__ = 'view_action'
    _id = db.Column(db.Integer, primary_key=True)
    _userId = db.Column(db.String(100), nullable=False)
    _sessionId = db.Column(db.String(100), nullable=False)
    _time = db.Column(db.String(100), nullable=False)
    _viewedId = db.Column(db.String(100), nullable=False)
