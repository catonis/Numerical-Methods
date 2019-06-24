# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 23:21:19 2019

@author: Chris Mitchell
"""

def AstroHMS2DecHours(hours, minutes, seconds):
    """Convert H:M:S or D°M'S" to either H.FRAC or D.FRAC.
    Takes three integers or floats and returns a float.
    """
    
    if minutes < 0 or seconds < 0:
        raise Exception("Negatives allowed only for first argument.")
    
    if hours < 0: sign = -1
    else: sign = 1
    
    hours = abs(hours)
    
    decMinutes = seconds / 60
    totalMinutes = decMinutes + minutes
    
    decHours = totalMinutes / 60
    totalHours = decHours + hours
    
    totalHours *= sign
    
    return totalHours


def AstroDecHours2HMS(decimalHours):
    """Convert H.FRAC or D.FRAC to standard representation as either
    H:M:S or D°M'S". This function takes a float and returns a tuple of
    two integers for hours and minutes and an integer or float for
    seconds.
    """
    
    from math import floor, modf
    
    if decimalHours < 0: sign = -1
    else: sign = 1
    
    decimalHours = abs(decimalHours)
    
    hours = floor(decimalHours)
    fractionalHours, _ = modf(decimalHours)
    minutes = floor(60 * fractionalHours)
    fractionalMinutes, _ = modf(60 * fractionalHours)
    seconds = 60 * fractionalMinutes
    
    hours *= sign
    
    #Adjust seconds for rounding error
    if abs(seconds - round(seconds)) < (10 ** -6):
        seconds = round(seconds)
    
    return hours, minutes, seconds
    
    
def AstroDecHours2DecDay(decimalHours):
    """Takes a decimal time of day and returns the fractional day.
    Takes a float and returns a float.
    """
    
    return decimalHours / 24

def AstroGDate2JDate(year, month, day):
    """The function takes a date in the Gregorian calendar and returns the
    Julian day number, which is the number of days having elapsed since
    January 1, 4713 BCE. Takes the year, month, and day in the Gregorian
    calendar as integers and returns the Julian day as an integer.
    """
    
    if month > 2:
        y = year
        m = month
    else:
        y = year - 1
        m = month + 12
    
    if year < 0:
        timeOffset = 0.75
    else:
        timeOffset = 0.0
    
    #Check if the date is Gregorian, that is, before October 15, 1582
    if year < 1582:
        gregorian = False
    elif year == 1582 and month < 10:
        gregorian = False
    elif year == 1582 and month == 10 and day < 15:
        gregorian = False
    else:
        gregorian = True
        
    if gregorian:
        yearOffset = 2 - int(y / 100) + int(int(y / 100) / 4)
    else:
        yearOffset = 0
    
    #The formula for calculating the Julian day. The formula simply totals
    #the days since January 1st of the first year CE and adds them to the
    #constant 1,720,994.5, which is the number of days since 0000h, January
    #1, 4713.
    julianDay = yearOffset + int((365.25 * y) - timeOffset) + \
                    int(30.6001 * (m + 1)) + day + 1720994.5
                    
    return julianDay


def AstroJDate2GDate(julianDate):
    """The funciton converts the Julian day number to its date in the
    Gregorian calendar. If the resulting Gregorian year in BCE, then
    the integer value for the Gregorian year will be a negative number.
    The function takes a float and returns the corresponding year and
    month, both as integers, and day, which may be either a float or integer.
    """
    
    from math import modf
    
    julianDate += 0.5
    
    decimalJD, integerJD = modf(julianDate)
    
    if integerJD > 2299160:
        a = int((integerJD - 1867216.25) / 36524.25)
        yearOffset = integerJD + 1 + a - int(a / 4)
    else:
        yearOffset = integerJD
    
    dayVarC = yearOffset + 1524
    dayVarD = int((dayVarC - 122.1) / 365.25)
    dayVarE = int(dayVarD * 365.25)
    dayVarF = int((dayVarC - dayVarE) / 30.6001)
    gregorianDay = dayVarC - dayVarE + decimalJD - int(30.6001 * dayVarF)
    
    if dayVarF < 13.5:
        gregorianMonth = dayVarF - 1
    else:
        gregorianMonth = dayVarF - 13
    
    if gregorianMonth > 2.5:
        gregorianYear = dayVarD - 4716
    else:
        gregorianYear = dayVarD - 4715
    
    #Adjust day in case of rounding error.
    if abs(gregorianDay - round(gregorianDay)) < (10 ** -6):
        gregorianDay = round(gregorianDay)
    
    return gregorianYear, gregorianMonth, gregorianDay
    
    
    