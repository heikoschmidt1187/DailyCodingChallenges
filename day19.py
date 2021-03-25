#!/bin/python3
"""
A builder is looking to build a row of N houses that can be of K different colors.
He has a goal of minimizing cost while ensuring that no two neighboring houses
are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to
build the nth house with kth color, return the minimum cost which achieves this
goal.
"""
import sys

if __name__ == '__main__':
    # setup test data
    prices = \
    [[7, 3, 8, 6, 1, 2],
     [5, 6, 7, 2, 4, 3],
     [10, 1, 4, 9, 7, 6],
     [10, 1, 4, 9, 7, 6]]
    
    N = len(prices)
    K = len(prices[0])

    # wie loop over the houses and modify the prices in the matrix in place
    # to avoid taking the same color the two lowest prices of the previous
    # house need to be remembered
    prev_house_min = 0
    prev_house_2nd_min = 0
    
    # we also need to remember k of the previous smallest price
    k_prev = -1
    
    # loop over houses
    for n in range(N):
        cur_house_min = sys.maxsize
        cur_house_2nd_min = sys.maxsize
        k_min = 0

        # loop over colors, get min and adapt prices
        for k in range(K):
            
            # if same k as previous, take 2nd lowest
            if k == k_prev:
                prices[n][k] += prev_house_2nd_min
            else:
                prices[n][k] += prev_house_min

            # take care to retrieve the min price of the current house
            if cur_house_min > prices[n][k]:
                cur_house_2nd_min = cur_house_min
                cur_house_min = prices[n][k]
                k_min = k
            elif cur_house_2nd_min > prices[n][k]:
                cur_house_2nd_min = prices[n][k]

        # prepare next round
        prev_house_min = cur_house_min
        prev_house_2nd_min = cur_house_2nd_min
        k_prev = k_min
            
    print(min(prices[N - 1]))