from flask import jsonify, request
import datetime
import json
import re
from ..db import Database
from ..utils.hash_password import hash
from flask_restful import Resource

col = Database().get_db()
    


class Register(Resource):
    response= {'status': 400, "message": "Unable to register", "id": None}
    def post(self):
        user = json.loads(request.data)
        username = user['username']
        password = user['password']
        dummy = password
        email = user['email']
        password = hash(password)
        uname = col.find_one({'username': username})
        if uname:
            return jsonify({'status': 'failure', 'error': 'Username already exists'})
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            return jsonify({'status': 'failure', 'error': 'Invalid email address'})
        elif not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', dummy):
            return jsonify({'status': 'failure',
                            'error': 'Password must contain at least 8 characters, 1 uppercase, 1 lowercase, '
                                     '1 number and 1 special character'})
        elif not re.match(r'[A-Za-z0-9]+', username):
            return jsonify({'status': 'failure', 'error': 'Username must contain only letters and numbers'})
        else:
            user_dict = {'username': username, 'email': email, 'password': password,
                         'date': datetime.datetime.now()}
            status = col.insert_one(user_dict)
            self.response["status"] = 200
            self.response["message"] = "Registration successful"
            self.response["id"] = str(status.inserted_id)
            return self.response, 200
