#!/bin/python3
"""
Given an array of integers and a number k, where 1 <= k <= length of the array, 
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get:
[10, 7, 8, 8], since:

    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place and
you do not need to store the results. You can simply print them out as you compute
them.
"""
from collections import deque

if __name__ == '__main__':
    # idea: use a sliding window approach
    numbers = [10, 5, 2, 7, 8, 7]
    k = 3
    
    if k == 1:
        print(numbers)
    elif k == len(numbers):
        print([max(numbers)])
    else:
        window_max_elements = list()
        
        # create a queue and insert the first k elements from the array
        dq = deque()
        for i in range(k):
            while dq and numbers[dq[-1]] < numbers[i]:
                dq.pop()
            dq.append(i)

        # the largest element of first window is found
        window_max_elements.append(numbers[dq[0]])

        # loop over rest of elements, sliding the window further
        for i in range(k, len(numbers)):
            # remove elements out of the queue that are left of
            # the window -- O(k) space
            while dq and dq[0] <= i - k:
                dq.popleft()

            # same like in beginning, add greatest element
            while dq and numbers[dq[-1]] < numbers[i]:
                dq.pop()
            dq.append(i)

            window_max_elements.append(numbers[dq[0]])
            
        print(window_max_elements)
        