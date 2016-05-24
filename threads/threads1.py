"""
Notes: =========================================================================
Notes: Threading.
Notes:      Thread(target=<target method>, args=(arg1, arg2, ...))
Notes:
Notes: t.start() to start the thread.
Notes: t.join() makes the caller thread to wait until the callee thread exits.
Notes:
Notes: tl.acquire() blocks until it acquire the lock.
Notes: tl.release() releases the lock, if acquired.
Notes:
Notes: time.time() gives current time.
Notes: time.ctime() converts given time into ascii format.
Notes:
"""

import threading
import time

tLock = threading.Lock()

def timer(name, delay, repeat):
    print "Timer: %s started" %(name)
    while repeat > 0:
        time.sleep(delay)
        tLock.acquire()
        print name," has acquired the lock"
        print "%s : %s" %(name, time.ctime(time.time()))
        tLock.release()
        print name," has released the lock"
        repeat -= 1
    print "Timer: %s stopped" %(name)


def Main():
    t1 = threading.Thread(target=timer, args=("Timer1", 1, 5))
    t2 = threading.Thread(target=timer, args=("Timer2", 2, 5))

    t1.start()
    t2.start()

    # Wait for thread1 to complete
    t1.join()
    print "Main completed"


#===============================================================================
if __name__ == "__main__":
    Main()
