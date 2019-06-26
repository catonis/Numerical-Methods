# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 02:00:09 2019

@author: Chris Mitchell
"""

#Summation - Returns the sum of vector elements
def VectSummation(vector):
    
    sum = 0
    for element in vector:
        sum += element
        
    return sum


#DotProduct - Returns the dot product of two vectors
def VectDotProduct(vector1, vector2):
    
    if len(vector1) != len(vector2):
        raise Exception("Passed vectors are of different dimensions.")
    
    dotProduct = 0
    for a in range(len(vector1)):
        dotProduct += vector1[a] * vector2[a]
        
    return dotProduct


#Euclidian Norm - Returns the vector length
def VectEuclideanNorm(vector, tail = 0):
    
    from math import sqrt
    
    #If passed a vector tail of different dimension than the vector head,
    #raise an exception.
    if tail != 0 and len(tail) != len(vector):
        raise Exception("Passed vectors are of different dimensions.")
    
    length = 0
    
    #If tail = 0, we calculate the vector length as if the tail is at
    #the origin.    
    if tail == 0:
        for i in vector:
            length += i ** 2
    #If the tail is specified, measure the distance from head to tail.
    else:
        for i in range(len(vector)):
            length += (vector[i] - origin[i]) ** 2
    
    return sqrt(length)
    

#Matrix Multiplication
def MatxSquareMultiplication(matrixA, matrixB):
    
    n = len(matrixA)
    
    matrixC = []
    for i in range(n):
        matrixCRow = []
        for j in range(n):
            c = = 0
            for k in range(n):
                c += matrixA[i][k] * matrixB[k][j]
            matrixCRow.append(c)
        matrixC.append(matrixCRow)
    
    return matrixC
            
            
    