import time
from pyfingerprint.pyfingerprint import PyFingerprint

class Scanner:
    def __init__(self):
        self.state = 0

    def rfid_authresident(self, url, key):
        print(config.get_mac())
        data = {}
        data["mac"] = config.get_mac()
        data["value"] = key

        headers = {
            'Content-Type': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',

        }