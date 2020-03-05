import os
import requests
import json

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
    if response == 200:
        print(response)
        if response.text:
            msg = json.loads(response.text)
            return msg
        #     if msg["state"] == "success":
        #         return 1
        # return 0
    return {'state': "error","message":"no response form Oneplace"}

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
    return send(config["api"]["stamp"]["url_add"], oData)
    #
    # print(oData)
    # print("logged")