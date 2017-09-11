#!/usr/bin/env python3

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    # res = processRequest(req)

    # res = json.dumps(res, indent=4)
    # print(res)
    #r = make_response(res)
    #r.headers['Content-Type'] = 'application/json'
    #return r

def processRequest(req):
    if req.get("result").get("action") != "retail.inventory":
        
        return {}

