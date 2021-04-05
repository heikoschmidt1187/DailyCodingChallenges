#!/bin/python3
"""
You are given an array of non-negative integers that represents a two-dimensional
elevation map where each element is unit-width wall and the integer is the height.
Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1)
space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in
the second, and 3 in the fourth index (we cannot hold 5 since it would run off
to the left), so we can trap 8 units of water.
"""
def get_max_volume(walls):
    # we need at least three walls to catch water
    if len(walls) < 3:
        return 0
    
    # we go from left to right and sum up the water to be caught
    total_volume = 0
    l = 0
    r = len(walls) - 1
    
    # remember the maximum height for left and right seen until now
    l_max = 0
    r_max = 0
    
    while l <= r:
        if walls[l] < walls[r]:
            # check if current left wall is higher than the seen
            if walls[l] > l_max:
                l_max = walls[l]
            else:
                # we can add water
                total_volume += l_max - walls[l]
                
            # continue left to right
            l += 1
                
        else:
            # check if current right wall is higher than the seen
            if walls[r] > r_max:
                r_max = walls[r]
            else:
                # we can add water
                total_volume += r_max - walls[r]

            r -= 1
            
    return total_volume

if __name__ == '__main__':
    walls = [2, 1, 2]
    print(get_max_volume(walls))

    walls = [3, 0, 1, 3, 0, 5]
    print(get_max_volume(walls))
    