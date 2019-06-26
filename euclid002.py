# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 21:05:29 2019

@author: Chris Mitchell
"""

#Create a list of Fibonacci numbers up to the limit of 4 x 10^16.
#Processor time is saved by creating a list of Fibonacci numbers first
#and keeping it in memory.

fibList = [1, 2]
breakInt = 100
for i in range(2, breakInt):
    newFibNum = fibList[-1] + fibList[-2]
    fibList.append(newFibNum)
    if newFibNum > 4 * 10 ** 16: break

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    #Find the index of the highest Fibonacci number less than n and sum
    #the even Fibonacci numbers along the way.

    evenSum = 0
    for i in fibList:
        if i > n: break
        if i % 2 == 0: evenSum += i
    print(evenSum)
