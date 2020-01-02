# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 05:42:25 2020

@author: Chris Mitchell
"""

def isPandigital(number):
    
    x = len(str(number))
    if x > 9: return False
    digits = [i for i in range(1, x + 1)]
    numDigits = [int(char) for char in str(number)]
    if digits == numDigits: return True
    return False