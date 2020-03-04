import time
import os
import json
import sys

__author__  = "Juerg Binggeli <juerg.binggeli@gmail.com>"
__status__  = "development"
__version__ = "0.0.2"
__date__    = "04.03.2020"

def start():
    print("start")

if __name__ == "__main__":
    _startTime = time.time()
    config = json.load(open(os.path.dirname(__file__) + '/config.json'))
    print(sys.argv[1])
