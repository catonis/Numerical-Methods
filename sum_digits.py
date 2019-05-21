# -*- coding: utf-8 -*-
"""
Created on Mon May 20 22:42:40 2019

@author: cdm18
"""

def sumDigits(number):
    """Sum the digits of a given number."""
    
    #Convert the number to an iterable
    numberString = str(number)
    #Return -1 if the string is not a number.
    if not numberString.isdigit(): return -1
    
    #Sum the digits.
    digitSum = 0
    for i in numberString:
        digitSum += int(i)
    
    return digitSum
