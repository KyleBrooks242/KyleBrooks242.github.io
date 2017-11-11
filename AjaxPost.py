#!/usr/bin/env python
from flask import render_template
     
    
@app.route('/predictAccident', methods=['POST'])
def predictAccident():
    val =  request.form['key'];
    val2 = request.form['key2'];
    return json.dumps({'status':'OK','key':val,'key2':val2});