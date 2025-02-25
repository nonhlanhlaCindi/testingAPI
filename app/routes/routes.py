from flask import Blueprint
from app.controllers.user_controller import signup_controller, get_users_controller,signin_controller

bp = Blueprint('bp', __name__)

bp.route('/signup', methods=['POST'])(signup_controller)
bp.route('/signin', methods=['POST'])(signin_controller)
bp.route('/users', methods=['GET'])(get_users_controller)
