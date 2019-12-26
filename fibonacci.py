# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 02:01:44 2019

@author: Chris Mitchell
"""

def Fibonacci(breakInt):
    
    fibList = [0, 1]
    for i in range(2, breakInt):
        newFibNum = fibList[-1] + fibList[-2]
        fibList.append(newFibNum)
        if newFibNum > 4 * 10 ** 16: break
    return fibList