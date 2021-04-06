#!/bin/python3
"""
The edit distance between two strings refers to the minimum number of character
insertions, deletions, and substitutions required to change one string to the
other. For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""
def edit_distance(w1, w2):
    l1, l2 = len(w1), len(w2)
    man = 0
    
    # edge case 1 - insert all chars from second
    if l1 == 0:
        return l2

    # edge case 2 - delete all chars from first
    if l2 == 0:
        return l1
    
    # normal case - loop through shortest number of index and 
    for i in range(min(l1, l2)):

        # different chars lead to action 
        if w1[i] != w2[i]:
            man += 1
        
    # the length difference leads to addition / deletion
    man += abs(l1 - l2)

    return man

if __name__ == '__main__':
    w1 = 'kitten'
    w2 = 'sitting'
    print(edit_distance(w1, w2))

    w1 = ''
    w2 = 'sitting'
    print(edit_distance(w1, w2))

    w1 = 'kitten'
    w2 = ''
    print(edit_distance(w1, w2))
    
