# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 06:05:41 2019

@author: Chris Mitchell

Find the sum of the multiples of 3 and 5 below n. Input is the number of
test cases followed by n.

Input:  2
        10
        100
        
Output: 23
        2318
"""

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    """
    The brute-force approach takes too long - O(n):

        runningSum = 0
        for i in range(3, n):
            if i % 3 == 0 or i % 5 == 0:
                runningSum += i
        print(runningSum)

    What's required is to use Gauss' prodigal method:

         95 + 90 + 85 + ...
      +   5 + 10 + 15 + ...
      = 100 +100 +100 + ... / 2

         99 + 96 + 93 + ...
      +   3 +  6 +  9 + ...
      = 102 +102 +102 + ... / 2

    The final step is to remove the intersection of the two sets of divisors.
    This runs in constant time - O(1):
    """

    n -= 1
    numberOf5s = n // 5
    numberOf3s = n // 3
    sumOf5s = (numberOf5s * ((numberOf5s * 5) + 5)) // 2
    sumOf3s = (numberOf3s * ((numberOf3s * 3) + 3)) // 2
    total = sumOf3s + sumOf5s
    
    #Remove all the 15s as they have been counted twice.
    if n >= 15:
        numberOf15s = n // 15 
        sumOf15s = (numberOf15s * ((numberOf15s * 15) + 15)) // 2
        total -= sumOf15s
    print(total)


