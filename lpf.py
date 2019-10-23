# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 02:13:17 2019

@author: Chris Mitchell

Find the largest prime factor of a given number.
"""

from math import ceil, sqrt

number = 65535

#Even numbers (aside from 2) are not prime factors
while number % 2 == 0:
    number //= 2

#Therefore, start at 3, increment by 2, and divide N down until left
#with the largest prime factor.
i = 3
j = ceil(sqrt(number))
while True:
    while number % i == 0 and number != i:
        number //= i
    if i > j: break;
    else: i += 2

print(number)