# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 02:00:24 2019

@author: Chris Mitchell
"""


def StatsMean(population):
    """Calculates the mean of the population. Takes a list of values and
    returns a float.
    
    StatsMean takes a list of numbers (rationals, integers, or a mixture
    of both) and returns the statistical mean or average of all the values
    as a float.
    """
    
    total = 0
    for i in population:
        total += i
        
    return total / len(population)
    

def StatsMedian(population):
    """Calculates the median of the population. Takes a list of values
    and returns a float.
    
    StatsMedian takes a list of numbers (rationals, integers, or a mixture
    of both) and returns the median, or middle value, of the population.
    If there are     two middles values, i.e., the population contains an
    even number of elements, the mean of those two values is taken as the
    median. The median is returned as a float.
    """
    
    population.sort()
    
    #If the population has an even number of data points, take the mean
    #of the middle two values.
    if len(population) % 2 == 0:
        median = (population[len(population) // 2] + \
                  population[(len(population) // 2) - 1]) / 2
    #If the population has an odd number of data points, use the middle value.
    else:
        median = population[len(population) // 2]
        
    return median


def StatsMode(population):
     """Calculates the mode of the population. Takes a list of values and
     returns a float.
    
    StatsMode takes a list of numbers (rationals, integers, or a mixture
    of both) and returns the mode. The mode is the element appearing most
    often in the population. If two or more elements share the same maximum
    count, the lowest values element is returned. The return value is a float.
    """
    
    #Build a dictionary to count equal data points.
    countDict = {}
    for i in population:
        if i in countDict: countDict[i] += 1
        else: countDict[i] = 1

    #Calculate the mode of the population.
    maxMode = 0
    maxIndex = 0
    for k, v in countDict.items():
        #Select the value with the most occurances in the population.
        if v > maxMode:
            maxMode = v
            maxIndex = k
        #If two or more elements share the same count, find the lowest.
        elif v == maxMode and k < maxIndex:
            maxIndex = k
    
    return float(maxIndex)


def StatsQuartiles(population):
     """Calculates the first, second, and third quartiles of the population.
     Takes a list of values and returns a tuple of three floating point
     numbers.
    
    StatsQuartiles takes a list of numbers (rationals, integers, or a mixture
    of both) and calculates the quartiles. The first quartile is calculated
    as A[low...median]. The second quartile is the median of initial
    population. The third quartile is calculated as A[median + 1...high].
    The three quartiles, first, second, and third are returned as a tuple of
    floats.
    """
    
    population.sort()

    #The first quartile is the median of A[low...median]
    firstQuartile = StatsMedian(population[:len(population) // 2])
    #The second quartile is the median of the population.    
    secondQuartile = StatsMedian(population)
    
    #The thirds quartile is the median of A[median + 1...high]
    if len(population) % 2 == 0:
        thirdQuartile = StatsMedian(population[len(population) // 2:])
    else:
        thirdQuartile = StatsMedian(population[(len(population) // 2) + 1:])
        
    return firstQuartile, secondQuartile, thirdQuartile

    
def StatsVariance(population):
     """Calculates the variance of the population. Takes a list of values
     and returns the variance as a float.
    
    StatsVariance takes a list of numbers, rationals, integers, or both,
    and returns the variance of the population. The variance being
    the sum of the distances of each element to the mean squared.
    This number is also represented in statistics as sigma squared:
        
        sigma ** 2 = Sum from i = 0 to n of [(population[i] - mean) ** 2]
        
    The variance is returned as a float or integer depending on the
    elements of the population.
    """
    
    mean = StatsMean(population)
    
    summation = 0
    for i in range(len(population)):
        summation += (population[i] - mean) ** 2
    
    return summation / len(population)


def StatsStandardDeviation(population):
    """Calculates the standard deviation of the population. Takes a list
    of values and returns a float.
    
    StatsStandardDeviation takes a list of numbers, rationals, integers,
    or both, and returns the standard deviation of the population. The
    standard deviation being the square root of the sum of the distances
    of each element to the mean squared. This number is also represented
    in statistics as sigma:
        
        sigma = sqrt(Sum from i = 0 to n of [(population[i] - mean) ** 2])
        
    With the aforementioned StatsVariance, calculating the standard
    deviation is simply taking the square root of the variance.  The
    standard deviation is returned as a float or integer depending on the
    elements of the population.
    """
    
    from math import sqrt
    
    #Simply return the square root of the variance.
    return sqrt(StatsVariance(population))


def StatsnCk(n, k):
    """Returns the binomial coefficient of the kth term of (1 + x)^n,
    also known as n choose k. This also gives us the number of combinations
    selecting k items from n without repitition where order does not
    matter. Takes two integers, n and k, and returns the coefficient as
    an integer.
    """
    
    from math import factorial
    
    return(factorial(n) / (factorial(k) * factorial(n - k)))
    
    
def StatsnPk(n, k):
    """Returns the number of permutations selecting k items from n without
    repitition where order matters. Takes two integers, n and k, and
    returns the number of combinations as an integer.
    """
    
    from math import factorial
    
    return(factorial(n) / factorial(n - k))
    

def StatsBinomialDistribution(successNumber, totalTrials, probabilityOfSuccess):
    """Returns the result of a particular binomial experiment. Takes two
    integers, successNumber and totalTrials, and a float, probabilityOfSuccess,
    and returns a float.
    
    The binomial distribution is the probability distribution for the
    binomial random variable, given by the following probability mass
    function:
        
        b(x, n, p) = nCx * p^x * q^(n - x)
        
    Where q is equal to 1 - p.
    """
    
    probabilityOfFailure = 1 - probabilityOfSuccess
    
    probability = StatsnCk(totalTrials, successNumber) * \
                     (probabilityOfSuccess ** successNumber) * \
                     (probabilityOfFailure ** (totalTrials - successNumber))
                     
    return probability


def StatsGeometricDistribution(totalTrials, probabilityOfSuccess):
    """Returns the result of a statistical experiment with geometric
    distribution. Takes one integer, totalTrials, and one float,
    probabilityOfSuccess, and returns a float.
    
    The geometric distribution is a negative binomial distribution where
    the number of successes is . We express this with the following formula:
        
        g(n, p) = q^(n - 1) *  p
        
    Where p is 1 - q.
    """
    
    probabilityOfFailure = 1 - probabilityOfSuccess
    
    return((probabilityOfFailure ** (totalTrials - 1)) * probabilityOfSuccess)
    
