"""
Author: Guillermo Gutierrez
Date: January 23, 2016
Version: 1
File: reader.py
Description: This file reads into the raspberry pi
"""
import requests

def read_control(ip="10.251.75.127"):
    return requests.get("http://" + ip + ":5000/control").text
