#!/usr/bin/env python3

# Patches needed for flask and flask_restplus
from werkzeug.utils import cached_property
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from collections.abc import MutableMapping
import collections
collections.MutableMapping = MutableMapping
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask import Flask, request
from flask_restplus import Resource, Api
import json
import requests

app = Flask(__name__)
api = Api(app)

# HTTP post to route /api/v1/ping with a JSON key value pair
#
# Request header
#   {'Content-Type': 'application/json'}
# Request data
#   {"url": "http://example"}
# Response
#   The response.text of a requests.get from the above URL
@api.route('/api/v1/ping', methods=['POST'])
class ApiV1Ping(Resource):
  def post(self):
    dictionary = json.loads(request.data)
    response = requests.get(dictionary['url'])
    return response.text

# HTTP get from route /health
#
# Response
#   "OK" on success 
@api.route('/health', methods=['GET'])
class Health(Resource):
  def get(self):
    return "OK"

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8080)
