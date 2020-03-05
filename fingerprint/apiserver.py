import time
import os
import json
import sys
from flask import Flask,request,jsonify
from fingerprint import oneplace

__author__  = "Juerg Binggeli <juerg.binggeli@gmail.com>"
__status__  = "development"
__version__ = "0.0.2"
__date__    = "04.03.2020"

config = None
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'state': "no access"})


@app.route('/api/stamp', methods=['POST'])
def worktime_stamp():
    # content = request.json
    content = request.get_json()

    oRc = oneplace.logStamp(1, content['type'])
    # return content
    return jsonify({'state': oRc})



def start():
    global config
    try:
        with open("config.json") as json_data_file:
            config = json.load(json_data_file)
    except:
        print("File not found")
        exit(0)
    oneplace.init(config)
    print("Start Worktime Stamp")
    app.run(debug=True, host='0.0.0.0', port=config["api"]["server"]["port"])


# if __name__ == "__main__":
#     _startTime = time.time()
#     config = json.load(open(os.path.dirname(__file__) + '/config.json'))
#     print(sys.argv[1])
