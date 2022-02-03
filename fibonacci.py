#!C:\Users\cdm18\anaconda3\python.exe
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 02:01:44 2019

@author: Chris Mitchell

A Fibonacci sequence generator.
"""

def yieldFibonacci():
    """
    A simple iterator to yield the Fibonacci sequence, starting at 1.

    Yields
    ------
    int
        The next number in the Fibonacci sequence.

    """
    yield 1
    a = 1
    b = 2
    while True:
        yield b
        a, b = b, a + b
