#!/bin/python3
"""
Implement a job scheduler which takes in a function f and an integer n,
and calls f after n milliseconds.
"""

import threading
import time

class Scheduler():
    def __init__(self):
        # save the function object and the target timestamp 
        self.functions = []
        
        s = threading.Thread(target=self.schedule)
        s.start()
        
    # this scheduler function checks on a regular base which function
    # need to run and executes them
    def schedule(self):
        while True:
            
            # get timestamp in ms
            now = time.time() * 1000
            
            # loop over all scheduled functions and call if due
            for fun,ts in self.functions:
                if now > ts:
                    fun()
                    
            # remove called functions
            self.functions = [(fun, ts) for (fun, ts) in self.functions if ts > now]
            
            # sleep a small slice of time
            time.sleep(0.01)
    
    # this function is used to add function calls with delay to
    # the scheduler
    def add(self, f, n):
        print("Add function ", f, " at ", time.time() * 1000, "ms delay ", n, " ms")
        self.functions.append((f, time.time() * 1000 + n))
        
def testfunction():
    print('Run at ', time.time() * 1000, 'ms')

if __name__ == '__main__':
    sched = Scheduler()

    sched.add(testfunction, 100)
    sched.add(testfunction, 200)
    sched.add(testfunction, 400)
