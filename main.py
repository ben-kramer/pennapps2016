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

app = Flask(__name__)

@app.route('/control', methods=['POST'])
def control_service():
    request.form.get("")
    pass

@app.route('/video', methods=['POST'])
def video_service():
    pass

if __name__=='__main__':
    app.run()
