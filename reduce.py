# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 00:22:40 2018

@author: Chris Mitchell
"""

def reduce(numerator, denominator):
    """Reduce the fraction defined as numerator/denominator to its
       simplest form. Takes two integers and returns two integers as
       a tuple (numerator, denominator)."""
       
    #Immediately return 1/1 if the numerator and denominator
    #are equal.
    if numerator == denominator: return 1, 1
    
    #Set x and y to be the larger and smaller of the numerator and
    #denominator respectively. This sets us up to use a version of
    #Euclid's Algorithm
    x, y = max(numerator, denominator), min(numerator, denominator);
    
    while True:
        
        #Replace x with the remainder of x/y
        x %= y
        
        #When the remainder of x/y is zero, the gcd has been found.
        if x == 0: break
    
        #Make sure x remains the greater of the two numbers and
        #rerun the algorithm.
        if x < y: x, y = y, x
    
    #Return as integers the reduced fraction which is now
    #p/y and q/y.
    return int(numerator/y), int(denominator/y)
