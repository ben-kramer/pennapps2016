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

app = Flask(__name__)
r = ar.arduino_reader()

@app.route('/control')
def control_service():
    return next(r)

@app.route('/video', methods=['POST'])
def video_service():
    pass

if __name__=='__main__':
    app.run()
