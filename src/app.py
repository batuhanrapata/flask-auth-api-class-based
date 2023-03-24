from flask import Flask
from dotenv import load_dotenv
import os
from .routes import routes
from flask_restful import Api

load_dotenv()

app=Flask(__name__)
api = Api(app)
routes(api)

