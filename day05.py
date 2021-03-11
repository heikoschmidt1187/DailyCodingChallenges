#!/bin/python3
"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and 
last element of that pair. For example, car(cons(3, 4)) returns 3, and 
cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""

# cons is a closure that constructs a pair using a given function
def cons(a, b):
    # inner function pair builds the pair based on a given function f
    # f therefore defines >how< the pair is created
    def pair(f):
        return f(a, b)
    return pair

# get the first element of the pair
def car(c):
    # we need a function to forward to the pair function in cons
    # that is used to return the first value
    def first(a, b):
        return a
    
    # put the function to the closure and return the result
    return c(first)

# get the second element of the pair - same principle as car
def cdr(c):
    def second(a, b):
        return b 
    return c(second)

if __name__ == '__main__':
    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)))