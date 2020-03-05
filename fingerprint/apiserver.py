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
    # content = request.json
    print(request)
    print(request.json)
    print(request.data)
    # content = request.get_json()
    content=request.get_json(force=True)
    print(content)
    oRc = {'state': "error", 'message': "no valid data"}
    if content is not None:
        oRc = oneplace.logStamp(1, content['type'])
    # return content
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
    app.run(debug=True, host='localhost', port=config["api"]["server"]["port"])


# if __name__ == "__main__":
#     _startTime = time.time()
#     config = json.load(open(os.path.dirname(__file__) + '/config.json'))
#     print(sys.argv[1])
