# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 02:44:17 2019

@author: Chris Mitchell
"""

def numberAsWords(number, language="English"):
    """Translates an integer to an English language string."""
    
    wordDict = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "ninetten",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand"}

    numString = ""
    if number > 1000:
        return numString
    
    ones = number % 10
    tens = number % 100 // 10
    hundreds = number % 1000 // 100
    
    if number >= 0 and number < 20:
        numString = wordDict[number]
    elif number >= 20 and number < 100:
        if ones == 0:
            numString = wordDict[number]
        else:
            numString = wordDict[tens * 10] + "-" + wordDict[ones]
    elif number >= 100 and number < 1000:
        numString = wordDict[hundreds] + " " + wordDict[100]
        if ones == 0 and tens == 0:
            pass
        elif ones == 0:
            numString += " and " + wordDict[tens * 10]
        elif tens == 0:
            numString += " and " + wordDict[ones]
        else:
            if number % 100 > 0 and number % 100 < 20:
                numString += " and " + wordDict[number % 100]
            else:
                numString += " and " + wordDict[tens * 10] + "-" + wordDict[ones]
    elif number == 1000:
        numString = wordDict[1] + " " + wordDict[1000]
        
    return numString
