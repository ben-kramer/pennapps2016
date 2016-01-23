"""
Author: Guillermo Gutierrez
Date: January 23, 2016
Version: 1
Description: This file reads in the data from the arduino and returns it
"""
import serial

def read_control(usb_port='/dev/tty.usbmodemFA131'):
    s = serial.Serial(usb_port, 9600)
    while True:
			yield s.readline()
