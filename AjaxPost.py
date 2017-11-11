import os
from flask import Flask,render_template, request,json

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to Python Flask!'

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username'];
    password = request.form['password'];
    return json.dumps({'status':'OK','user':user,'pass':password});
    
@app.route('/test', methods=['GET', 'POST'])
def test():
    vars = request.data
    return ', '.join([str(i) for i in vars])

@app.route('/test2/',methods=['POST', 'GET'])
def ajaxcalc():
    vars = request.data
    return ', '.join([str(i) for i in vars])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')