#!/usr/bin/env python3

from datetime import datetime
import json

from flask import Flask

app = Flask(__name__)

@app.route("/")
def populate_bar():
    payload = {
        "time": get_time()
    }
    return json.dumps(payload)

def get_time():
    time = datetime.now()
    return time.strftime("%a %b %d %H:%M:%S CST %Y")