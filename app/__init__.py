import os
from flask import Flask
from flask_cors import CORS
from .routes.routes import main as main_blueprint
from .extensions import db, migrate
from .config.config import config

def create_app():
    app = Flask(__name__)
    
    env = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config[env])
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Registro das rotas
    app.register_blueprint(main_blueprint)
    
    return app
