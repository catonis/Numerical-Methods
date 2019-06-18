# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 02:00:24 2019

@author: Chris Mitchell
"""

#Mean - Returns the mean (average) of the population.
def StatsMean(population):
    
    total = 0
    for i in population:
        total += i
        
    return total / len(population)
    

#Median - Returns the median of the population.
def StatsMedian(population):
    
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


#Mode - Returns the mode of the population
def StatsMode(population):
    
    #Build a dictionary to count equal data points.
    countDict = {}
    for i in population:
        if i in countDict: countDict[i] += 1
        else: countDict[i] = 1

    #Calculate the mode of the population.
    maxMode = 0
    maxIndex = 0
    for k, v in countDict.items():
        if v > maxMode:
            maxMode = v
            maxIndex = k
        elif v == maxMode and k < maxIndex:
            maxIndex = k
    
    return maxIndex


#Quartiles - Returns a tuple of length three containing the
#first, second (median), and third quartiles.
def StatsQuartiles(population):
    
    population.sort()

    firstQuartile = StatsMedian(population[:len(population) // 2])    
    secondQuartile = StatsMedian(population)
    
    if len(population) % 2 == 0:
        thirdQuartile = StatsMedian(population[len(population) // 2:])
    else:
        thirdQuartile = StatsMedian(population[(len(population) // 2) + 1:])
        
    return firstQuartile, secondQuartile, thirdQuartile

    
#Variance - Returns the variance of the population.
def StatsVariance(population):
    
    mean = StatsMean(population)
    
    summation = 0
    for i in range(len(population)):
        summation += (population[i] - mean) ** 2
    
    return summation / len(population)


#Standard Deviation - Returns the standard deviation of the population.
def StatsStandardDeviation(population):
    
    from math import sqrt
    
    return sqrt(StatsVariance(population))
