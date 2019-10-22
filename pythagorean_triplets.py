# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 04:29:57 2019

@author: Chris Mitchell

A Pythagorean triplet is a set of three natural numbers, a < b < c,
for which, a ** 2 + b ** 2 = c ** 2

For example, 3 ** 2 + 4 ** 2 = 9 + 16 = 25 = 5 ** 2.

The function getTriplets(limit) returns all Pythagorean triplets up to
c = limit.

"""

def getTriplets(limit):
    c, m = 0, 2

    triplets = []
    while c < limit:    
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            if c > limit: break

            triplets.append([a, b, c])
        m = m + 1
    return triplets