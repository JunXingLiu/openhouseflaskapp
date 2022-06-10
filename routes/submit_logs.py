from flask import Blueprint, copy_current_request_context, jsonify, make_response, request
import threading

from ..models.click_action import ClickAction
from ..models.view_action import ViewAction
from ..models.navigate_action import NavigateAction
from ..extensions import db

submitLogs = Blueprint('submitLogs', __name__)

@submitLogs.route('/submitlogs', methods=['POST'])
def create_logs():
    @copy_current_request_context
    def create_logs_task():
        data = request.get_json()
        create_log_entries(data)
    threading.Thread(target=create_logs_task).start()
    return make_response(jsonify({'status': 'logs submitted'}), 200)

def create_log_entries(data):
    entries = []
    error = []
    userId = data.get('userId')
    sessionId = data.get('sessionId')
    actions = data.get('actions')
    for action in actions:
        time = action.get('time')
        actionType = action.get('type')
        if actionType.lower() == 'click':
            locationX = action.get('properties').get('locationX')
            locationY = action.get('properties').get('locationY')
            click = ClickAction(_userId = userId, 
                                _sessionId = sessionId, 
                                _time = time, 
                                _locationX = locationX, 
                                _locationY = locationY)
            entries.append(click)
        elif actionType.lower() == 'view':
            viewedId = action.get('properties').get('viewedId')
            view = ViewAction(_userId = userId, 
                              _sessionId = sessionId, 
                              _time = time, 
                              _viewedId = viewedId)
            entries.append(view)
        elif actionType.lower() == 'navigate':
            pageFrom = action.get('properties').get('pageFrom')
            pageTo = action.get('properties').get('pageTo')
            navigate = NavigateAction(_userId = userId, 
                                      _sessionId = sessionId, 
                                      _time = time, 
                                      _pageFrom = pageFrom, 
                                      _pageTo = pageTo)
            entries.append(navigate)
        else:
            error.append(actionType + ' is an invalid action type')
    db.session.bulk_save_objects(entries)
    db.session.commit()
    return error
