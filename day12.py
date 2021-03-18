#!/bin/python3
"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps
at a time. Given N, write a function that returns the number of unique ways you
can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways.
- 1,1,1,1
- 2,1,1
- 1,2,1
- 1,1,2
- 2,2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any
number from a set of positive integers X? For example, if X = {1, 3, 5}, you could
climb 1, 3 or 5 steps at a time.
"""

"""
Base idea is that to calculate the variants to reach a given step, the variants
of the sums to reach previous steps can be reused
"""
def get_num_ways(N, X):
    # base case - no steps, there's only one variant to "step up"
    if N == 0:
        return 1
    
    # sum of ways to reach for each step
    nums = [0 for _ in range(N + 1)]
    nums[0] = 1     # again, the base case

    # loop over all steps and calculate how to reach them
    for i in range(1, N+1, 1):
        total = 0
        
        # loop over all possible ways to step and check if with 
        # the value a given step can be reached
        for x in X:
            # if current step minus steps to take is lower than 0, it means
            # we would step up too far
            if i - x >= 0:
                total += nums[i - x]
                
        nums[i] = total
        
    return nums[N]

if __name__ == '__main__':
    N = 4
    X = {1, 2}
    
    print(get_num_ways(N, X))