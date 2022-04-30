#!/usr/bin/env python3
from flask import Flask
import json

app = Flask(__name__)
@app.route('/api/v1/info')

def index():
  return json.dumps({'Receiver': 'Cisco is the best!'})

app.run()