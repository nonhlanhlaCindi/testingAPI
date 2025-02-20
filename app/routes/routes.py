from flask import Blueprint
from app.controllers.user_controller import create_user_controller, get_users_controller  #type: ignore


bp = Blueprint('bp', __name__)


bp.route('/create', methods=['POST'])(create_user_controller)
bp.route('/users', methods=['GET'])(get_users_controller)


