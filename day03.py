#!/bin/python3
"""
Given the root to a binary tree, implement serialize(root), which serializes 
the tree into a string, and deserialize(s), which deserializes the string
back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
import re

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def serialize(root):
    # add delimiter and root value
    s = '{' + root.val + ','
            
    # depending on if left node present, serialize it or set None
    if root.left is None:
        s += 'None'
    else:
        s += serialize(root.left)
        
    s += ','

    # depending on if right node present, serialize it or set None
    if root.right is None:
        s += 'None'
    else:
        s += serialize(root.right)

    # close node
    s += '}'

    return s

def deserialize(s):
    # extract node data
    node_match = re.match(r'^\{(\w+)\,(.*)\}$', s)
    node = Node(node_match.group(1))

    left_right_match = re.match(r'(\{.*\})\,(\{.*\})', node_match.group(2))

    if left_right_match:
        if left_right_match.group(1) is not None:
            node.left = deserialize(left_right_match.group(1))

        if left_right_match.group(2) is not None:
            node.right = deserialize(left_right_match.group(2))
    
    return node
        
if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'