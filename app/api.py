"""
api.py  
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request, send_file

api = Blueprint('api', __name__)

@api.route('/hello/<string:name>/')
def say_hello(name):  
    response = { 'msg': "Hello {}".format(name) }
    return jsonify(response)

@api.route('others')
def others():
        return jsonify({'file': 'value'})
        return send_file('others-fixed.mp3', attachment_filename='others-fixed.mp3')