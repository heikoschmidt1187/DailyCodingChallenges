#!/bin/python3
"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a
Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.
"""
import random
import math

if __name__ == '__main__':
    """
    The idea is to take one quadrant of the unit circle, emit points at random
    and check through the circle equation if which vertices are in and out of
    the circle. For a quadrant area of unit circle: A = π/4
    = points in circle/all emitted points
    """
    random.seed(a = None, version = 2)
    pt_cnt = 10000000
    inlier_cnt = 0

    # generate points at random in quadrant
    for i in range(pt_cnt):
        if math.sqrt(random.random()**2 + random.random()**2) <= 1:
            inlier_cnt += 1

    # calculate pi
    print('Pi: {:.4}'.format(4 * (inlier_cnt / pt_cnt)))