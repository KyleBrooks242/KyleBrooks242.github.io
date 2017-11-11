import os
from flask import Flask,render_template, request,json

app = Flask(__name__)

@app.route('/predictIncident', methods=['POST'])
def predictIncident():
    dayOfWeek =  request.form['dayOfWeek']
    time = request.form['time']
    lat = request.form['lat']
    long = request.form['long']
    
    return json.dumps({'status':'OK'});

if __name__=="__main__":
    app.run()