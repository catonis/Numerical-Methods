# -*- coding: utf-8 -*-
"""
Created on Mon May 20 02:33:19 2019

@author: Chris Mitchell
"""

def getPrimes(breakInt = 10 ** 9):

    from math import sqrt, ceil, floor
    
    primeList = [2, 3, 5]
    sieve = [False] * (breakInt + 1)
    
    for x in range(1, ceil(sqrt(breakInt)) + 1):
        for y in range(1, ceil(sqrt(breakInt)) + 1):
            n = 4 * x ** 2 + y ** 2
            if n <= breakInt and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 + y ** 2
            if n <= breakInt and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 - y ** 2
            if x > y and n <= breakInt and n % 12 == 11:
                sieve[n] = not sieve[n]
    
    for x in range(7, floor(sqrt(breakInt))):
        if sieve[x]:
            for y in range(x ** 2, breakInt + 1 , x ** 2):
                sieve[y] = False
    for i in range(7, breakInt):
        if sieve[i]:
            primeList.append(i)
    return primeList