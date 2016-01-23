"""
Author: Guillermo Gutierrez
Date: January 23, 2016
Version: 1
Description: This file reads in the data from the arduino and returns it
"""
import serial

def arduino_reader():
    s = serial.Serial('/dev/tty.usbmodemFA131', 9600)
    while True:
			yield s.readline()

def main():
    arduino_read()

if __name__ == '__main__':
    main()
