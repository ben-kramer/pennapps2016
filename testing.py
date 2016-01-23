import time
import arduino_reader as ar
def testing(calls_per_second=10):
    start = time.time()
    period = 1.0/calls_per_second
    r = ar.arduino_read()
    while True:
        if (time.time()-start) > period:
            print next(r)
            start = time.time()

