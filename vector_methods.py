# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 02:00:09 2019

@author: Chris Mitchell
"""


def Summation(vector):
    """Simply sum the elements of the vector.
    
    Summation takes a vector passed in as a list and returns the sum of
    the elements of the vector.
    """
    
    sum = 0
    for element in vector:
        sum += element
        
    return sum


def DotProduct(vector1, vector2):
    """Calculates the dot product of two vectors.
    
    Returns the dot product of two equally sized vectors. This value
    is the sum of the products of equally indexed elements in the vector.
    The return value is a float or an integer depending on the field
    of the vectors.
    """"
    
    #If the vectors are different sizes, the dot product is undefined.
    if len(vector1) != len(vector2):
        raise Exception("Passed vectors are of different dimensions.")
    
    dotProduct = 0
    for a in range(len(vector1)):
        dotProduct += vector1[a] * vector2[a]
        
    return dotProduct


def EuclideanNorm(vector, tail = 0):
    """Calculate the Euclidean norm or length of the given vector.
    
    This function assumes that the tail of the vector is at the origin.
    If the tail is at a different set of coordinates than the origin,
    it can be passed in as a second list. The length of the vector is
    returned as a float or integer depending on the coordinates.
    """
    
    from math import sqrt
    
    #If passed a vector tail of different dimension than the vector head,
    #raise an exception.
    if tail != 0 and len(tail) != len(vector):
        raise Exception("Passed vectors are of different dimensions.")
    
    length = 0
    
    #If tail = 0, we calculate the vector length as if the tail is at
    #the origin.    
    if tail = 0:
        for i in vector:
            length += i ** 2
    #If the tail is specified, measure the distance from head to tail.
    else:
        for i in range(len(vector)):
            length += (vector[i] - origin[i]) ** 2
    
    return sqrt(length)
    
