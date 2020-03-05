import os
import json
import requests
config = None

def init(configFile):
    global config
    config = configFile

def send(url, data):
    headers = {
        "Content-Type": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    response = requests.post(url, headers=headers, data=data)
    msg = json.loads(response.text)
    if msg["state"] == "success":
        return 1
    return 0

def logStamp(finger,type):
    # set data to send to OnePlace
    sType = ""
    if type == 1:
        sType = "Kommen"
    elif type == 2:
        sType = "Gehen"
    else:
        sType = "Unknown"

    oData = {}
    values = {}
    values["label"] = "raspi"
    values["finger"] = finger
    values["type"] = sType
    oData["authkey"] = config["api"]["key"]
    oData["authtoken"] = config["api"]["token"]
    oData["values"] = json.dumps(values)
    send(config["api"]["stamp"]["url_add"], oData)

    print(oData)
    print("logged")