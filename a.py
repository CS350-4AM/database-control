from threading import Timer
import time

timeout = 0.5

while(True):
    t = Timer(timeout, print, ['Sorry, times up'])
    t.start()
    time.sleep(2)
    print('1')
    t.cancel()
