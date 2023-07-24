#from flask import Flask, render_template, jsonify, request
#import requests

#app = Flask(__name__)

#@app.route('/')
#def index():
#    return render_template('index.html')

#@app.route('/get_joke')
#def get_joke():
#    category = request.args.get('category')
#    if category:
#        response = requests.get(f"https://api.chucknorris.io/jokes/random?category={category}")
#    else:
#        response = requests.get("https://api.chucknorris.io/jokes/random")
#    joke_data = response.json()
#    return jsonify({'joke': joke_data['value']})

#if __name__ == '__main__':
#    app.run(debug=True)










from flask import Flask
#from flask_restful import Api
#from db import db

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask1156!!!"

if __name__== "__main__":
    app.run(host='0.0.0.0' , port=5000 , debug = True)    
#if __name__ == '__main__':
    # Run the app on port 8000
#    app.run(port=8000)     
