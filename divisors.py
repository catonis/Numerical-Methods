# -*- coding: utf-8 -*-
"""
Created on Mon May 20 22:35:51 2019

@author: cdm18
"""
from math import sqrt

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

def primeDivisors(number):
    """Returns a list of the prime factorization of a number."""

    primeFactors = []    
    candidates = divisors(number)
    for i in candidates:
        isPrime = True
        for j in range(2, i):
            if i % j == 0: isPrime = False
        if isPrime: primeFactors.append(i)
        
    return primeFactors

def countDivisors(number):
    """Returns the number of factors for a given number."""
    
    numFactors = 0
    squareRoot = int(sqrt(number))
    
    for i in range(1, squareRoot):
        if number % i == 0:
            numFactors += 2
    
    if squareRoot * squareRoot == number:
        numFactors -= 1
        
    