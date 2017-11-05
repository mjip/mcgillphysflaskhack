from flask import Flask
app = Flask(__name__)
import json
from flask import request, jsonify, render_template
import pot2d as pot

def parse_data(data):
    values = []
    # There are 3 values per point
    for i in range(1,6):
        val = []
        val.append(float(data['x'+str(i)]))
        val.append(float(data['y'+str(i)]))
        val.append(float(data['q'+str(i)]))
        values.append(val)
    if 'zoom' in data:
        zoom = data['zoom']
    else:
        zoom = [-10.0,10.0,-10.0,10.0]
    if 'flag' in data:
        flag = data['flag']
    else:
        flag = 0
    if 'scheme' in data:
        scheme = data['scheme']
    else:
        scheme = 'viridis'
    return values, zoom, flag, scheme

@app.route("/load_data", methods=["GET", "POST"])
def load_data():
    data = request.form
    values, zoom, flag, scheme = parse_data(data)
    pot.findPotential(values, zoom, flag, scheme)
    return json.dumps({'status':'OK','data':values},);

@app.route("/")
def hello():
    return render_template('index.html')
 


''' 
@app.route('/run')
def signUp():
    return render_template('index.html')    
'''

if __name__ == "__main__":
    app.run()
    
