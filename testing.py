import time
import arduino_reader as ar
import requests

def speed(calls_per_second=10):
    start = time.time()
    period = 1.0/calls_per_second
    r = ar.arduino_reader()
    while True:
        if (time.time()-start) > period:
            print next(r)
            start = time.time()

def remote():
    print requests.get("http://127.0.0.1:5000/control").text
