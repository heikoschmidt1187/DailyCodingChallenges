#!/bin/python

"""
Given an array of integers, return a new array such that each element at 
index i of the new array is the product of all the numbers in the original 
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output 
would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

if __name__ == '__main__':
    # test 1 - in_array = [3, 2, 1]
    # test 2 - in_array = [1, 2, 3, 4, 5]
    in_array = [1, 2, 3, 4, 5]
    out_array = []

    # this is the solution without division - it runs with O(n²)
    for i in range(len(in_array)):
        prod = 1
        
        for j in range(len(in_array)):
            if i != j:
                prod *= in_array[j]
            
        out_array.append(prod)
    
    print(out_array)
    
