# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 20:55:39 2018

@author: Chris Mitchell
"""

from reduce import reduce


def unpack_cont(cont_frac):
    """Take a continued fraction and expand it to a rational number.
       The function takes a continued fraction as a list and unpacks
       the fraction which is returned as a tuple
       (numerator, denominator)."""
    
    #If we are at the end of the list, simply return the
    #reciprocal of the last fraction.
    if len(cont_frac) == 1:
        return cont_frac[0], 1
    
    #Now we recursively call the function so that we can move
    #backwards from the end of the list and calculate the fraction.
    else:
        
        #First collect the numerator and denominator from
        #the recursive call
        new_den, new_num = unpack_cont(cont_frac[1:])
        
        #Return a tuple containing the reciprocal of
        #the fraction calculated by adding the next integer
        #off the list added to the previously returned
        #fraction.
        return cont_frac[0] * new_den + new_num, new_den
    
    
def pack_cont(num, den):
    """Creates a continued fraction representation of the passed
       in fraction. The fraction is passed in as a tuple,
       (numerator, denominator), and a list containing the
       continued fraction representation of the fraction is
       returned."""
    
    #First we reduce the fraction if possible.
    num, den = reduce(num, den)
   
    #If the fraction is 1/1, return [1]. If the
    #fraction is 0/1, return [0].
    if (num, den) == (1, 1): return [1]
    elif (num, den) == (0, 1): return [0]

    #Initialize an empty list, cf, to contain the continued
    #fraction.
    cf = []
   
    #Use a while loop to continue to generate terms for the
    #continued fraction until the fraction represents a
    #whole number.
    while den != 1:
        
        #If we begin with a fraction less than one, we must
        #first append a 0 to the list.
        if num < den: cf.append(0)
            
        #Else we append the integer division result between
        #the numerator and denominator.
        else: cf.append(num // den)
            
        #Now we change the numerator to the remainder of
        #the integer division and procede with the reciprocal.
        num, den = den, num % den
        
    #We must capture the final value of the numerator and
    #append it to the list.
    cf.append(num)
    
    #Return the list.
    return cf
