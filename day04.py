#!/bin/python
"""
Given an array of integers, find the first missing positive integer in 
linear time and constant space. In other words, find the lowest positive 
integer that does not exist in the array. The array can contain 
duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0]
should give 3.

You can modify the input array in-place.
"""

def restructure_list(numbers):
    """
    The smallest positive integer for n = len(numbers) has to be in set
    {1, 2, ..., n, n+1} (Pigeonhole Principle). So ignore all numbers outside
    [1, n+1].
    
    Through this, the general idea is that we can use the array indices to 
    track already seen integers as it's the same size. This needs a re-sorting
    so all valid positive integers are filled up at array's front. All elements
    out of range are moved to back.
    """
    n = len(numbers)
    front = 0
    end = n - 1
    
    while front < end:
            # outside range elements are swaped to the back of the array
            if (numbers[front] < 1) or (numbers[front] > n):
                t = numbers[front]
                numbers[front] = numbers[end]
                numbers[end] = t
                end -= 1
            else:
                front += 1
                
    return numbers, front if numbers[front] >= 1 and numbers[front] <= n else front - 1

def find_lowest_positive_missing_int(numbers):
    """
    Basic idea is that with a restructured list where all numbers in [1...n+1] are located
    at front and the rest at the end of the array, the elements serve as index in the array.
    So for every seen element, the sign is flipped to negative to mark as seen. The first
    element with positive sign then is the smallest integer. If all are negative, the smallest
    integer is n+1.

    This works because we want the smallest POSITIVE integer.
    """
    numbers, in_range = restructure_list(numbers)
    
    # in case none of the numbers is in [1...n+1], the smallest positive integer is 1
    if in_range < 0:
        return 1
    
    # flip the sign for seen indices
    for i in range(0, in_range + 1, 1):
        idx = abs(numbers[i]) - 1
        numbers[idx] = -abs(numbers[idx])
    
    # check for positive index
    for i in range(len(numbers)):
        if numbers[i] >= 0:
            return i + 1
        
    # not positive value found
    return len(numbers) + 1

if __name__ == '__main__':
    #numbers = [3, 4, -1, 1]
    #numbers = [-4, 3, 0, 2, 1]
    #numbers = [1, 2, 0]
    numbers = [-9, 9, 1, 2, 5]
    print(find_lowest_positive_missing_int(numbers))