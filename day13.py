#!/bin/python3
"""
Given an integer k and a string s, find the length of the longest substring
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct
characters is "bcb".
"""

def get_dist_substring(k, s):
    # if no characters allowed, return
    if k == 0:
        return 0
    
    max_len = 0

    # we build a window over the string bound by the indices of the lowest
    # and the highest bound
    window_bounds = (0, 0)

    # the unique characters inkl. index will be traces in a dict
    char_dict = {}

    for i, ch in enumerate(s):
        # add the new character
        char_dict[ch] = i
        
        # if the length of the dictionary is below the given k, we can safely
        # add the char
        if len(char_dict) <= k:
            low_bound = window_bounds[0]
        else:
            # get the character with the min index and pop it
            pop = min(char_dict, key=char_dict.get)
            low_bound = char_dict.pop(pop) + 1

        # reset the bounds to the new lower one left and incremented upper bound right
        window_bounds = (low_bound, window_bounds[1] + 1)
        max_len = max(max_len, window_bounds[1] - window_bounds[0])
        
    return max_len
    

if __name__ == '__main__':
    k = 2
    s = 'abcba'
    
    print('Length of longest distinct substring: ', get_dist_substring(k, s))