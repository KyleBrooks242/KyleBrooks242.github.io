import os
from flask import Flask,render_template, request,json

app = Flask(__name__)

@app.route('/predictIncident', methods=['POST'])
def predictIncident():
    user =  request.form['username'];
    password = request.form['password'];
    return json.dumps({'status':'OK','user':user,'pass':password});

<<<<<<< HEAD
if __name__=="__main__":
    app.run()
=======
@app.route('/kylebrooks242.github.io/test2/',methods=['POST', 'GET'])
def ajaxcalc():
    vars = request.data
    return ', '.join([str(i) for i in vars])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> branch 'master' of https://github.com/KyleBrooks242/KyleBrooks242.github.io.git
