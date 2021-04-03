#!/bin/python
"""
Given a string of round, curly, and square open and closing brackets, return 
whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""
def is_balanced(s):
    stack = []
    d = {']': '[', ')': '(', '}': '{'}

    for c in s:
        if c in d:
            o = stack.pop()
            if o != d[c]:
                return False
        else:
            stack.append(c)
            
    return len(stack) == 0

if __name__ == '__main__':
    s = '([])[]({})'
    print(is_balanced(s))
    
    s = '([)]'
    print(is_balanced(s))

    s = '((()'
    print(is_balanced(s))
    