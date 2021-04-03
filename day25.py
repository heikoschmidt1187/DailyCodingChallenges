#!/bin/python3
"""
Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular
expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your
function should return true. The same regular expression on the string
"raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should
return true. The same regular expression on the string "chats" should return false.
"""
def match_first(s, re):
    # matches if first character is equal or any-character
    return (s[0] == re[0]) or (re[0] == '.' and len(s) > 0)

def regex(s, re):
    # this is a recursive problem, matching the heads of the re with the heads of 
    # the string

    # base case - if re is empty, s must be empty, too
    if re == '':
        return s == ''

    # if next char in regex is not followe by '*', compare the next one
    if len(re) == 1 or re[1] != '*':
        if match_first(s, re):
            # go down recursive
            return regex(s[1:], re[1:])
        else:
            return False
    else:
        # we have a * as next character, so first check if no aditional char
        if regex(s, re[2:]):
            return True

        # if it doesn't match, check for repeating chars
        i = 0
        while match_first(s[i:], re):
            # try to match now
            if regex(s[i+1:], re[2:]):
                return True
            i += 1
            
    return False
        

if __name__ == '__main__':
    s = 'ray'
    re = 'ra.'
    print(regex(s, re))

    s = 'raymond'
    re = 'ra.'
    print(regex(s, re))
    
    s = 'chat'
    re = '.*at'
    print(regex(s, re))
    