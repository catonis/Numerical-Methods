# -*- coding: utf-8 -*-
"""
Created on Mon May 20 22:35:51 2019

@author: cdm18
"""

def divisors(number):
    """Returns the positive integer factors of the given number as
       a list."""
    
    #1 is always a factor to a given integer.
    factors = [1]
    
    for n in range(2, (number // 2) + 1):
        if number % n == 0:
            factors.append(n)
    
    #A number is always a factor of itself
    factors.append(number)
    
    return factors
