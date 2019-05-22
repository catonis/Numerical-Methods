# -*- coding: utf-8 -*-
"""
Created on Wed May 22 05:33:15 2019

@author: cdm18
"""

def gcd(x, y):
    """Find the greatest common denominator betweeen x and y."""
    
    if x == y: return x

    while True:
        if x < y: x, y = y, x
        x %= y
        if x == 0: return y
