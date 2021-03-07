#!/bin/python

"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def check_sum(numbers, k):
    sums = []
    
    for n in numbers:
        # given that a sum has to be found, ignore improper values
        if n >= k:
            continue
        
        # check if a given number can be added up to k
        for s in sums:
            if s + n == k:
                return True 

        # at this point, remember current number
        sums.append(n)

    return False

if __name__ == '__main__':
    
    # list and search sum
    # test 1 - true: numbers = [10, 15, 3, 7]
    # test 2 - false: numbers = [20, 73, 19, 2]
    # test 3 - false: numbers = [5, 5, 7]
    # test 4 - true: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    k = 17
    
    print(check_sum(numbers, k))