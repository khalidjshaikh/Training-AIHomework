#!/usr/bin/env python3
from werkzeug.utils import cached_property
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from collections.abc import MutableMapping
import collections
collections.MutableMapping = MutableMapping
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
# import pdb; pdb.set_trace()
from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

# HTTP get from route /api/v1/info
#
# Response
#   {'Receiver': 'Cisco is the best!'}
@api.route('/api/v1/info')
class ApiV1Info(Resource):
  def get(self):
    return {'Receiver': 'Cisco is the best!'}

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8080)
