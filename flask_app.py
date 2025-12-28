import os
from app import create_app
from app.config import ProductionConfig, DevelopmentConfig

env = os.environ.get("FLASK_ENV", "development")

if env == "production":
    app = create_app(ProductionConfig)
else:
    app = create_app(DevelopmentConfig)
