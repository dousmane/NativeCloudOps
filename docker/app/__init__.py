from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate = Migrate(app, db)  # Initialisez Flask-Migrate ici

    with app.app_context():
        from . import routes
        routes.init_app_routes(app)

    return app

