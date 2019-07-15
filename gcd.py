# -*- coding: utf-8 -*-
"""
Created on Wed May 22 05:33:15 2019

@author: cdm18
"""

def gcd(x, y):
    """Find the greatest common denominator betweeen x and y,
    using Euclid's algorithm."""
    
    if x == y: return x

    while y: x, y = y, x % y
    return x


def gcdx(*args):
    """Find the greatest common denominator between all given numbers."""

    n = len(args) - 1
    j = args[n]
    for i in range(n - 1, -1, -1):
        j = gcd(args[i], j)

    return j
        
        
def lcm(x, y):
    """Find the least common multiple of x and y."""
    
    return (x * y) // gcd(x, y)


def lcmx(*args):
    """Find the least common multiple between all given numbers."""

    n = len(args) - 1
    j = args[n]
    for i in range(n - 1, -1, -1):
        j = (args[i] * j) // gcd(args[i], j)

    return j


    
