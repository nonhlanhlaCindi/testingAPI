from app.controllers.user_controller import create_user_controller, get_users_controller
from flask import Flask

app = Flask(__name__)


app.route('/create', methods=['POST'])(create_user_controller)
app.route('/users', methods=['GET'])(get_users_controller)

if __name__ == '__main__':
    app.run(debug=True)
