import time
import os
import json
import sys
from flask import Flask,request,jsonify
from flask_cors import CORS
from fingerprint import oneplace

__author__  = "Juerg Binggeli <juerg.binggeli@gmail.com>"
__status__  = "development"
__version__ = "0.0.2"
__date__    = "04.03.2020"

config = None
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def index():
    return jsonify({'state': "no access"})


@app.route('/api/stamp', methods=['POST'])
def worktime_stamp():
    form = request.form
    oRc = {'state': "error", 'message': "no valid data"}
    print(request)
    if form is None:
        form = request.param
    if form is not None:
        try:
            print(form['data'])
            oRc = oneplace.logStamp(1, form['data'])
        except Exception as e:
            print("exception occurred: " + str(e))
            return jsonify(oRc)
    print(oRc)
    return jsonify(oRc)



def start():
    global config
    try:
        with open("config.json") as json_data_file:
            config = json.load(json_data_file)
    except:
        print("Config.json not found")
        exit(0)
    oneplace.init(config)
    print("Start Worktime Stamp")
    print(config["api"]["server"]["url"])
    print(config["api"]["server"]["port"])
    app.run(ssl_context=('fullchain1.pem', 'privkey1.pem'), debug=True, host=config["api"]["server"]["url"], port=config["api"]["server"]["port"])

ssl_context=()
