#!/bin/bash

"""
A unival tree (which stands for "universal value") is a tree where all nodes 
under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def helper(bt):
    # if the given node is not an object, no subcount but unival tree
    if bt is None:
        return 0, True

    # count left and right unival trees and check unival status
    cnt_left, left_is_ut = helper(bt.left)
    cnt_right, right_is_ut = helper(bt.right)
    
    # total count at this point is the sum of unival trees
    total = cnt_left + cnt_right
    
    # depending on if the current note is root of a unival tree,
    # the count has to be adapted
    if left_is_ut and right_is_ut:
        # check if left and right continues this ut
        if bt.left is not None and bt.left.value != bt.value:
            return total, False
        if bt.right is not None and bt.right.value != bt.value:
            return total, False
        
        # each child node, if present, continues with the value 
        # of this bt
        return total + 1, True

    return total, False
    
        
def cnt_unival_tree(bt):
    count, _ = helper(bt)
    return count

if __name__ == '__main__':
    
    # test 1 tree - 5
    #bt = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    
    # test 2 tree - 3
    #bt = Node('a', Node('a'), Node('a', Node('a'), Node('a', None, Node('A'))))
    
    # test 3 tree - 5
    bt = Node('a', Node('c'), Node('b', Node('b'), Node('b', None, Node('b'))))
    
    count = cnt_unival_tree(bt)
    print('Unival trees: ', count)