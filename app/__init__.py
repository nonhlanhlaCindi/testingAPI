from flask import Flask
from config import get_db_connection  
from app.routes.routes import bp  #type: ignore

def create_app():
    app = Flask(__name__)

    
    from app.routes.routes import bp
    app.register_blueprint(bp)

    return app
