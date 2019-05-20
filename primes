# -*- coding: utf-8 -*-
"""
Created on Mon May 20 02:33:19 2019

@author: cdm18
"""

def yieldPrimes():
    """A generator that yields prime numbers"""

    yield 2
    
    primeCandidate = 3
    isPrime = True
    
    while primeCandidate:
        for divisor in range(2, primeCandidate // 2):
            if primeCandidate % divisor == 0: isPrime = False
        if isPrime: yield primeCandidate
        primeCandidate += 2
        isPrime = True
