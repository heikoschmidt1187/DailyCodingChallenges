#!/bin/python3
"""
Implement locking in a binary tree. A binary tree node can be locked or unlocked
only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

- is_locked, which returns whether the node is locked
- lock, which attempts to lock the node. If it cannot be locked, then it should
    return false. Otherwise, it should lock it and return true.
- unlock, which unlocks the node. If it cannot be unlocked, then it should return
    false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like.
You may assume the class is used in a single-threaded program, so there is no need
for actual locks or mutexes. Each method should run in O(h), where h is the height
of the tree.
"""

class Node():
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.locked = False
        self.locked_descendents = 0
    
    def _can_lock_or_unlock(self):
        # if any descendent is locked, not possible
        if self.locked_descendents > 0:
            return False

        # go up parents to check if there is any locked
        current_parent = self.parent
        
        while current_parent:
            if current_parent.is_locked():
                return False

            current_parent = current_parent.parent
            
        # none locked
        return True

    def is_locked(self):
        return self.locked

    def lock(self):
        # edge case - already locked
        if self.locked:
            return True

        # condition check
        if not self._can_lock_or_unlock():
            return False

        # lock the node and update the parent's counters
        self.locked = True

        current_parent = self.parent

        while current_parent:
            current_parent.locked_descendents += 1
            current_parent = current_parent.parent
            
        return True
    
    def unlock(self):
        """
        kind of same like locked, even if the check is not
        mandatory as through lock conditions it should not 
        happen that we are locked and any descendent or 
        ancestor is locked
        """
        if not self.locked:
            return True

        if not self._can_lock_or_unlock():
            return False

        self.locked = False

        current_parent = self.parent

        while current_parent:
            current_parent.locked_descendents -= 1
            current_parent = current_parent.parent
            
        return True
    

if __name__ == '__main__':
    tree = Node(1)

    n1 = Node(1, parent=tree)
    tree.left = n1
    
    n2 = Node(2, parent=n1)
    n1.left = n2

    n3 = Node(3, parent=n1)
    n1.right = n3
    
    n4 = Node(4, parent=tree)
    tree.right = n4
    
    n5 = Node(5, parent=n2)
    n2.left = n5


    print(tree.left.left.lock())
    print(tree.lock())
    print(tree.left.left.unlock())
    print(tree.lock())

            