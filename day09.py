#!/bin/python
"""
Given a list of integers, write a function that returns the largest sum of 
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

mem = {}

"""
My first solution by using a recursive approach. This has O(n) for time
and space.
"""
def find_max_nonadj_sum_recursive(numbers):
    # get length of current array
    n = len(numbers)

    # base case 1: empty array
    if n == 0:
        return 0

    # base case 2: only one element -- return 0 in case
    # the element is negative
    if n == 1:
        max(0, numbers[0])
        
    # recursive case, existing of three possibilities
    mem[n] = max(
        # the case where all other elements are negative, leading to smaller sum
        numbers[-1],
        
        # the case we take this element and continue with the next non-adjacent
        numbers[-1] + find_max_nonadj_sum_recursive(numbers[:-2]),

        # the case we don't use the current element and continue with the next
        find_max_nonadj_sum_recursive(numbers[:-1])
    )
    
    return mem[n]

"""
Second variant where recursion is eliminated
"""
def find_max_nonadj_sum_iterative(numbers):
    mem_it = {}
    
    # we need the two previous sums to continue on them
    mem_it[-2] = 0  
    mem_it[-1] = 0

    n = len(numbers)
    for i in range(n):
        mem_it[i] = max(
            # in case all already seen elements are negative, the current number is base
            numbers[i],
        
            # the case we take this element and the last non-adjacent
            numbers[i] + mem_it[i - 2],

            # the case we exclude this element and take the last adjacent
            mem_it[i - 1]
    )
        
    return mem_it[n - 1]

"""
This is an enhanced version of the iterative one as we really don't need the
whole sum history, but rather only the last two sums to stand on
"""
def find_max_nonadj_sum(numbers):
    prev_sum = 0
    prev_prev_sum = 0

    n = len(numbers)
    for i in range(n):
        curr_sum = max(
            # in case all already seen elements are negative, the current number is base
            numbers[i],
        
            # the case we take this element and the last non-adjacent
            numbers[i] + prev_prev_sum,

            # the case we exclude this element and take the last adjacent
            prev_sum
        )
        
        prev_prev_sum = prev_sum
        prev_sum = curr_sum
        
    return prev_sum

if __name__ == '__main__':
    # test 1: numbers = [2, 4, 6, 2, 5]
    # test 2: numbers = [5, 1, 1, 5]
    numbers = [5, 1, 1, 5]

    print('Max sum: ', find_max_nonadj_sum_recursive(numbers))
    print('Max sum: ', find_max_nonadj_sum_iterative(numbers))
    print('Max sum: ', find_max_nonadj_sum(numbers))