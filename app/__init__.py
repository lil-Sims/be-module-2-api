from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from typing import Type

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_class: Type) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    ma.init_app(app)

    from .routes import api_bp
    app.register_blueprint(api_bp)

    return app
