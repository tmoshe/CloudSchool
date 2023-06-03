from flask import Flask
#from flask_restful import Api
#from db import db

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask112!!!"

if __name__ == '__main__':
    # Run the app on port 8000
    app.run(port=5000)    
    
