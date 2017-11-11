import os
from flask import Flask,render_template, request,json

app = Flask(__name__)

@app.route('/predictIncident', methods=['POST'])
def predictIncident():
    user =  request.form['username'];
    password = request.form['password'];
    return json.dumps({'status':'OK','user':user,'pass':password});

if __name__=="__main__":
    app.run()