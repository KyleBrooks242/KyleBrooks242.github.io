#!/usr/bin/env python   
    
from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Welcome to Python Flask!"

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username'];
    password = request.form['password'];
    return json.dumps({'status':'OK','user':user,'pass':password});
 
if __name__ == "__main__":
    app.run()