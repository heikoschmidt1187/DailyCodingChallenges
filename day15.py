#!/bin/python3
"""
Given a stream of elements too large to store in memory, pick a random element 
from the stream with uniform probability.
"""
import random

def pick(stream):
    random.seed(a=None, version=2)
    
    # we only save the picked element as the stream size is unknown and
    # may not fit into memory
    element = None

    # simulate get of next element; with a real stream we have to look
    # at EOF and i is a separate variable to be incremented
    for i, e in enumerate(stream):
        
        # the first element is picked automatically as the stream may
        # have a length of 1
        if i == 0:
            element = e
            
        # to pick uniformly we want the chance to get picket to be 1/(i+1), so
        # we retrieve an integer out of i + 1 and take a specific value (== 1)
        # to trigger the actual picking
        elif random.randint(1, i + 1) == 1:
            element = e

    return element

if __name__ == '__main__':
    dummy_stream = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('Element: ', pick(dummy_stream))