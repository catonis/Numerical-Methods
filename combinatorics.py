# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 05:30:44 2019

@author: Chris Mitchell
"""

from math import factorial

def nCk(n, k):
    return factorial(n) // (factorial(n - k) * factorial(k))

def nPk(n, k):
    return factorial(n) // factorial(n - k)