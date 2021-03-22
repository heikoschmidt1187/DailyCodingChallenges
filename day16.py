#!/bin/python3
"""
You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be
        smaller than or equal to N.

You should be as efficient with time and space as possible.
"""
import random
from collections import deque

"""
In C/C++ I would use a (doubly) linked list and access the elements from
front or rear on a full list based on the requested get_last --> O(N/2) on time
for search, O(N) for space, O(1) for insert/remove

Here in Python, I just use a plain deque embedded in a log class, making the access
depending just on an index O(1), space O(N). Insert/remove depends on the implementation
in Python, bug is in general a shift of elements O(N) + append O(1)
"""
class Log():
    def __init__(self, N):
        self.log = deque([])
        self.N = N
        
    # record the latest order id
    def record(self, order_id):
        if len(self.log) >= self.N:
            self.log.popleft()
            
        self.log.append(order_id)

    def get_last(self, i):
        if i >= len(self.log):
            return 0

        return self.log[i]

if __name__ == '__main__':
    log = Log(10)
    random.seed(a=None, version=2)

    for i in range(100):
        log.record(random.randint(0, 100))
        
        l = []
        for i in range(10):
            l.append(log.get_last(i))
        print(l)
