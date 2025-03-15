from models.User import User
from flask import jsonify
from config import db
from flask_jwt_extended import create_access_token

def get_all_users():
    try:
        return [ user.to_dict() for user in User.query.all()]    
    except Exception as error:
        print(f"ERROR {error}")
                #return jsonify ({'msg' :  'error al obtener los datos faker '}), 500


def create_user(name, email, password):
    try:
        new_user = User(name, email, password)
    
        db.session.add(new_user)
        db.session.commit()
        
        return new_user.to_dict()

    except Exception as e:
        print(f"ERROR {e}")
        #return jsonify ({'msg' :  'error al crear usuario'}), 500

def update_user(user_id, name=None, email=None):
    try:
        user = User.query.get(user_id)
        if not user:
            return None

        if name:
            user.name = name
        if email:
            user.email = email

        db.session.commit()
        return user.to_dict()
    except Exception as e:
        print(f"ERROR {e}")

def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return None

        db.session.delete(user)
        db.session.commit()
        return {"message": "usuairo eliminado"}
    except Exception as e:
        print(f"ERROR {e}")

def login_user(email, password):
    user=User.query.filter_by(email=email).first();
    if User and user.check_password(password):
        acces_token = create_access_token(identity= user.id);
        return jsonify({
            'acces_token': acces_token,
            'user':{
                "id": user.id,
                "name": user.name,
                "email": user.email
 }
})  
#return jsonify ({"msg" : "credenciales invalidas"}), 401