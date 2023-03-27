from flask import Flask
#from flask_restful import Api
#from db import db

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask112!!!"
    