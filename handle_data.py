# -*- coding: utf-8 -*-
"""
Created on Sat Nov 04 19:24:14 2017

@author: Sacha Perry-Fagant
"""

import sys
import cgi
import json
import flask
from flask import request, jsonify, render_template
import sys
import cgitb
cgitb.enable()



@app.route("/load_data", methods=["GET", "POST"])
def load_data():
    values, zoom, flag, scheme = parse_data(request)
    return json.dumps({'status':'OK'});

'''
sys.stdout.write("Content-Type: application/json")
sys.stdout.write("\n") 
sys.stdout.write("\n")
form = cgi.FieldStorage() 
data = json.dumps({ 'data': form.getvalue('x1')})
sys.stdout.write(data)
'''

def parse_data(data):
    values = []
    # There are 3 values per point
    for i in range(1,6):
        val = []
        val.append(data['x'+str(i)])
        val.append(data['y'+str(i)])
        val.append(data['q'+str(i)])
        values.append(val)
        
    return values, 

load_data()