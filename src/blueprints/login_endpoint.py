from flask import jsonify, request,current_app
import json
import jwt
from ..db import Database
from ..utils.hash_password import verify
import os
from dotenv import load_dotenv
from flask_restful import Resource
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
col = Database().get_db()
    
class Login(Resource):
    response = {'status': 400, "message": "Unable to login", "id": None, "access_token": None}
    def post(self):
        user = json.loads(request.data)
        username = user['username']
        password = user['password']
        uname = col.find_one({'username': username})
        if uname:
            if verify(uname['password'], password):
                token = jwt.encode({'_id': str(uname['_id'])}, SECRET_KEY)
                self.response["status"] = 200
                self.response["message"] = "Login successful"
                self.response["id"] = str(uname['_id'])
                self.response["access_token"] = token
                return self.response, 200
        else:
            return self.response, 400


    
        
