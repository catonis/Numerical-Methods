# -*- coding: utf-8 -*-
"""
Created on Mon May 20 02:33:19 2019

@author: Chris Mitchell
"""

def yieldPrimes():
    """A generator that yields small prime numbers."""
    
    pass


def getPrimes(breakInt = 10 ** 9):
    """This function implements the Atkin-Bernstein sieve. The function
    itself takes an integer value which is the upper boundary for the
    search of primes. It returns all the primes from 2 to the boundary,
    which defaults to one billion.
    
    The sieve first assumes that all integers up to the boundary value
    are not prime. It then pushes the prime numbers through the "sieve"
    These are determined by examining the properties of solutions sets
    to three equations:  4x^2 + y^2 = n, 3x^2 + y^2 = n, and 3x^2 - y^2 = n.
    """

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
    
    for x in range(5, floor(sqrt(breakInt))):
        if sieve[x]:
            for y in range(x ** 2, breakInt + 1 , x ** 2):
                sieve[y] = False
    for i in range(7, breakInt):
        if sieve[i]:
            primeList.append(i)
    return primeList


def getGreatestPrimeDivisor(number):
    """Takes as an integer a number and return its largest prime divisor.
    """
    
    while number % 2 == 0:
        number //= 2

    i = 3
    j = ceil(sqrt(number))
    while True:
        while number % i == 0 and number != i:
            number //= i
        if i > j: break;
        else: i += 2

    return number


def getPrimeFactorization(number):
    """Takes as an integer a number and returns a list containing its
    prime factorization. For instance, calling the function with the
    number 20 will return a list [2, 2, 5].
    """
    
    factors = []
    limit = number // 2 + 1
    
    for i in range(2, limit):
        while number % i == 0:
            factors.append(i)
            number //= i

    return factors
