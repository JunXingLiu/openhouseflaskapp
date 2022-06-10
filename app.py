from flask import Flask

from extensions import db
from routes.submit_logs import submitLogs
from routes.retrieve_logs import retrieveLogs

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logs.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    app.register_blueprint(submitLogs)
    app.register_blueprint(retrieveLogs)

    return app

def __main__():
    app = create_app()
    app.run(debug=True)