"""
Notes: =========================================================================
Notes: Threading.
Notes:      Thread(target=<target method>, args=(arg1, arg2, ...))
Notes:
Notes: t.start() to start the thread.
Notes:
Notes: time.time() gives current time.
Notes: time.ctime() converts given time into ascii format.
Notes:
"""

from threading import Thread
import time

def timer(name, delay, repeat):
    print "Timer: %s started" %(name)
    while repeat > 0:
        time.sleep(delay)
        print "%s : %s" %(name, time.ctime(time.time()))
        repeat -= 1
    print "Timer: %s stopped" %(name)

def Main():
    t1 = Thread(target=timer, args=("Timer1", 1, 5))
    t2 = Thread(target=timer, args=("Timer2", 2, 5))

    t1.start()
    t2.start()

    print "Main completed"


#===============================================================================
if __name__ == "__main__":
    Main()
