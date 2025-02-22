from flask import Blueprint, jsonify, request
from controllers.userController import get_all_users, create_user, update_user, delete_user

user_bp = Blueprint('users', __name__)

@user_bp.route('/', methods=['GET'])
def index():
    users = get_all_users()
    return jsonify(users)

@user_bp.route('/', methods=['POST'])
def user_store():
    data = request.get_json()
    name = data.get('name')
    lastname = data.get('lastname')  # Capturar lastname
    email = data.get('email')

    print(f"NAME {name} --- LASTNAME {lastname} --- EMAIL {email}")
    new_user = create_user(name, lastname, email)
    return jsonify(new_user)

@user_bp.route('/<int:user_id>', methods=['PUT'])
def user_update(user_id):
    data = request.get_json()
    name = data.get('name')
    lastname = data.get('lastname')  # Capturar lastname
    email = data.get('email')

    updated_user = update_user(user_id, name, lastname, email)
    return jsonify(updated_user)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def user_delete(user_id):
    deleted_user = delete_user(user_id)
    return jsonify(deleted_user)
