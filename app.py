from flask import Flask
#from flask_restful import Api
#from db import db

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask1123!!!"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=4000 , debug=True)