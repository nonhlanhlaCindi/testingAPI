from flask import Flask
from config import get_db_connection  


def create_app():
    app = Flask(__name__)
    from app.routes.routes import bp
    app.register_blueprint(bp, url_prefix='/api')

    return app

