"""
Author: Guillermo Gutierrez
Date: January 23, 2016
Version: 1
File: main.py
Description: This file works as the middle man between the arduino and the
             raspberry pi
"""

from flask import Flask
from flask import request
import arduino_reader as ar
import string

app = Flask(__name__)
r = ar.read_control()

@app.route('/control')
def control_service():
    return string.join(string.split(next(r), " ")[:3], " ")

if __name__=='__main__':
    app.run(host = "10.251.75.127", debug=True)
