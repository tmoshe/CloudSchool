from flask import Flask
#from flask_restful import Api
#from db import db

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask113!!!"

if __name__== "__main__":
    app.run(host='0.0.0.0' , port=5000 , debug = True)    
#if __name__ == '__main__':
    # Run the app on port 8000
#    app.run(port=8000)     
