from flask import jsonify, request, current_app
from functools import wraps
import jwt
from bson import ObjectId
from ..db import Database
import os 
from dotenv import load_dotenv
from flask_restful import Resource
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
col = Database().get_db()




def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = col.find_one({'_id': ObjectId(data['_id'])})
        except Exception as e:
            return jsonify({'message': 'Token is invalid!', 'error': str(e)}), 401
        return f(current_user, *args, **kwargs)

    return decorated

@token_required
def get_all_users(current_user):
    if not current_user:
        return jsonify({'message': 'Cannot perform that function!'})
    users = col.find()
    output = []
    for user in users:
        user_data = {}
        user_data['username'] = user['username']
        output.append(user_data)
    return jsonify({'users': output})



class ListUsers(Resource):
    def get(self):
        return get_all_users()