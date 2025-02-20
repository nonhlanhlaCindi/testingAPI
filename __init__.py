from flask import Flask
from config import Config  
from app.controllers.user_controller import create_user_controller, get_users_controller  
from app.models.user import create_user, get_users  

def create_app():
    app = Flask(__name__)
    
   
    app.config.from_object(Config)
    

    app.add_url_rule('/create', 'create_user', create_user_controller, methods=['POST'])
    app.add_url_rule('/users', 'get_users', get_users_controller, methods=['GET'])
    
    return app
