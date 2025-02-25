from flask import request, jsonify
import bcrypt # type: ignore
from app.models.user import signup, signin, get_users

def signup_controller():
    data = request.get_json()

    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    password = data['password']

    success = signup(first_name, last_name, email, password)

    if success:
        return jsonify({'message': 'User created successfully'}), 201
    else:
        return jsonify({'message': 'User already exists with this email'}), 400


def get_users_controller():
    users = get_users()

    if users:
        return jsonify({'users': users}), 200
    else:
        return jsonify({'message': 'No users found'}), 404


def signin_controller():
    try:
        data = request.get_json() 
        email = data['email']
        password = data['password']

        user = signin(email, password) 
        
        if not user:
            return jsonify({'message': 'Invalid email or password'}), 401

        return jsonify({'message': 'Signin successful'}), 200

    except Exception as e:
        print(f"Error during signin: {str(e)}")
        return jsonify({'message': 'An error occurred during signin. Please try again later.'}), 500
