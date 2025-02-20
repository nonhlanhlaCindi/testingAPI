from flask import request, jsonify
from app.models.user import create_user, get_users #type: ignore


def create_user_controller():
    data = request.get_json()  

    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    password = data['password']

   
    success = create_user(first_name, last_name, email, password)

    if success:
        return jsonify({'message': 'User created successfully'}), 201
    else:
        return jsonify({'message': 'Error creating user'}), 500

def get_users_controller():
    users = get_users()  
    
    if users:
        return jsonify(users), 200
    else:
        return jsonify({'message': 'No users found'}), 404
