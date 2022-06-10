from dataclasses import dataclass

from extensions import db

@dataclass
class ClickAction(db.Model):
    _userId : str
    _sessionId : str
    _time : str
    _locationX : str
    _locationY : str

    __tablename__ = 'click_action'
    _id = db.Column(db.Integer, primary_key=True)
    _userId = db.Column(db.String(100), nullable=False)
    _sessionId = db.Column(db.String(100), nullable=False)
    _time = db.Column(db.String(100), nullable=False)
    _locationX = db.Column(db.String(100), nullable=False)
    _locationY = db.Column(db.String(100), nullable=False)