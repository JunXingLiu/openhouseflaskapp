from flask import Blueprint, jsonify, make_response, request

from models.click_action import ClickAction
from models.view_action import ViewAction
from models.navigate_action import NavigateAction
from extensions import db

retrieveLogs = Blueprint('/api/retrieveLogs', __name__)

@retrieveLogs.route('/api//retrievelogs', methods=['GET'])
def retrieve_logs():
    userId = request.args.get('userId')
    logType = request.args.get('logType')
    fromTime = request.args.get('fromTime')
    toTime = request.args.get('toTime')
    if not userId and not logType and (not fromTime or not toTime):
        return make_response(jsonify({'status': 'parameter(s) must be provided'}), 400)

    if userId and not logType and not fromTime and not toTime:
        logs = db.session.query(ClickAction).filter(ClickAction._userId == userId).all()
        logs.extend(db.session.query(ViewAction).filter(ViewAction._userId == userId).all())
        logs.extend(db.session.query(NavigateAction).filter(NavigateAction._userId == userId).all())
        return make_response(jsonify(logs), 200)
    
    if userId and logType and not fromTime and not toTime:
        if logType.lower() == 'click':
            logs = db.session.query(ClickAction).filter(ClickAction._userId == userId).all()
            return make_response(jsonify(logs), 200)
        elif logType.lower() == 'view':
            logs = db.session.query(ViewAction).filter(ViewAction._userId == userId).all()
            return make_response(jsonify(logs), 200)
        elif logType.lower() == 'navigate':
            logs = db.session.query(NavigateAction).filter(NavigateAction._userId == userId).all()
            return make_response(jsonify(logs), 200)
        else:
            return make_response(jsonify({'status': 'logType must be click, view, or navigate'}), 400)
    
    if userId and logType and fromTime and toTime:
        if logType.lower() == 'click':
            logs = db.session.query(ClickAction).filter(ClickAction._userId == userId).filter(ClickAction._time >= fromTime).filter(ClickAction._time <= toTime).all()
            return make_response(jsonify(logs), 200)
        elif logType.lower() == 'view':
            logs = db.session.query(ViewAction).filter(ViewAction._userId == userId).filter(ViewAction._time >= fromTime).filter(ViewAction._time <= toTime).all()
            return make_response(jsonify(logs), 200)
        elif logType.lower() == 'navigate':
            logs = db.session.query(NavigateAction).filter(NavigateAction._userId == userId).filter(NavigateAction._time >= fromTime).filter(NavigateAction._time <= toTime).all()
            return make_response(jsonify(logs), 200)
        else:
            return make_response(jsonify({'status': 'logType must be click, view, or navigate'}), 400)
    
    if not userId and logType and not fromTime and not toTime:
        if logType.lower() == 'click':
            logs = db.session.query(ClickAction).all()
            return make_response(jsonify(logs), 200)
        elif logType.lower() == 'view':
            logs = db.session.query(ViewAction).all()
            return make_response(jsonify(logs), 200)
        elif logType.lower() == 'navigate':
            logs = db.session.query(NavigateAction).all()
            return make_response(jsonify(logs), 200)
        else:
            return make_response(jsonify({'status': 'logType must be click, view, or navigate'}), 400)
    
    if not userId and logType and fromTime and toTime:
        if logType.lower() == 'click':
            logs = db.session.query(ClickAction).filter(ClickAction._time >= fromTime).filter(ClickAction._time <= toTime).all()
            return make_response(jsonify(logs), 200)
        elif logType.lower() == 'view':
            logs = db.session.query(ViewAction).filter(ViewAction._time >= fromTime).filter(ViewAction._time <= toTime).all()
            return make_response(jsonify(logs), 200)
        elif logType.lower() == 'navigate':
            logs = db.session.query(NavigateAction).filter(NavigateAction._time >= fromTime).filter(NavigateAction._time <= toTime).all()
            return make_response(jsonify(logs), 200)
        else:
            return make_response(jsonify({'status': 'logType must be click, view, or navigate'}), 400)
    
    if userId and not logType and fromTime and toTime:
        logs = db.session.query(ClickAction).filter(ClickAction._userId == userId).filter(ClickAction._time >= fromTime).filter(ClickAction._time <= toTime).all()
        logs.extend(db.session.query(ViewAction).filter(ViewAction._userId == userId).filter(ViewAction._time >= fromTime).filter(ViewAction._time <= toTime).all())
        logs.extend(db.session.query(NavigateAction).filter(NavigateAction._userId == userId).filter(NavigateAction._time >= fromTime).filter(NavigateAction._time <= toTime).all())
        return make_response(jsonify(logs), 200)
    
    if not userId and not logType and fromTime and toTime:
        logs = db.session.query(ClickAction).filter(ClickAction._time >= fromTime).filter(ClickAction._time <= toTime).all()
        logs.extend(db.session.query(ViewAction).filter(ViewAction._time >= fromTime).filter(ViewAction._time <= toTime).all())
        logs.extend(db.session.query(NavigateAction).filter(NavigateAction._time >= fromTime).filter(NavigateAction._time <= toTime).all())
        return make_response(jsonify(logs), 200)

