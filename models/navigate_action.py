from dataclasses import dataclass
from dataclasses import dataclass

from extensions import db

@dataclass
class NavigateAction(db.Model):
    _userId : str
    _sessionId : str
    _time : str
    _pageFrom : str
    _pageTo : str

    __tablename__ = 'navigate_action'
    _id = db.Column(db.Integer, primary_key=True)
    _userId = db.Column(db.String(100), nullable=False)
    _sessionId = db.Column(db.String(100), nullable=False)
    _time = db.Column(db.String(100), nullable=False )
    _pageFrom = db.Column(db.String(100), nullable=False)
    _pageTo = db.Column(db.String(100), nullable=False)