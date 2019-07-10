# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 21:54:53 2019

@author: Chris Mitchell
"""

class PalindromicInteger(int):
    _palindrome = 0
    _pLen = 0
    _pSplitIndex = 0
    _pIsLenEven = False
    _pSplits = []
    
    def __init__(self, n):
        self._palindrome = n
        self._pLen = len(str(self._palindrome))
        self._pSplitIndex = self._pLen // 2
        
        if self._pLen % 2 == 0:
            self._pIsLenEven = True
            self._pSplits = [int(str(self._palindrome)[:self._pSplitIndex]),
                             None,
                             int(str(self._palindrome)[self._pSplitIndex:])]
        else:
            self._pIsLenEven = False
            self._pSplits = [int(str(self._palindrome)[:self._pSplitIndex]),
                             int(str(self._palindrome)[self._pSplitIndex]),
                             int(str(self._palindrome)[self._pSplitIndex + 1:])]

    def __set__(self, instance, value):
        __init__(value)
    
    def __get__(self, instance, owner):
        return self._Palindrome
    
    def __len__(self):
        return len(str(self._palindrome))
    
    def getSplits(self):
        return self._pSplits[:]

def isPalindromic(palindrome):

    if str(palindrome) == str(palindrome)[::-1]: return True
    else: return False

            
def getGreatestPalindromicNumber(number):
    """Given an integer, this function will find the greatest
    palindromic number less than that integer.
    """
    
    number -= 1
    
    strN = str(number)
    lenN = len(strN)
    splitP = lenN // 2
    
    #Two procedures depending on whether or not the number of digits of
    #the original number is even or odd.
    if lenN % 2 == 0:
        
        #Make a palindrome that is less than the number and store it
        #in intP
        strP = str(int(strN[:splitP]) - 1)
        strP += strP[::-1]
        intP = int(strP)
        
        #Prepare to test against the next highest palindromic with
        #corrections for palindromics nearest a power of 10

        #This is how we count palindromics
        enumP = 11 ** (splitP - 1)
        
        #Generate the next highest palindromic
        testP = intP + enumP
        
        #Check if the number is indeed a palindromic. If it isn't,
        #it must be close to a power of 10
        if not isPalindromic(testP):
            strP = strN[:splitP]
            testP = int(strP + strP[::-1])
            
        if testP > number: palindromic = intP
        else: palindromic = testP
        
    else:
        
        strP = str(int(strN[:splitP + 1]) - 1)
        tmpStr = strP[:splitP]
        tmpStr = tmpStr[::-1]
        strP += tmpStr
        intP = int(strP)
        
        enumP = 10 ** splitP
        
        testP = intP + enumP
        
        if not isPalindromic(testP):
            strP = strN[:splitP + 1]
            tmpStr = strP[:splitP]
            testP = int(strP + tmpStr[::-1])
            
        if testP > number: palindromic = intP
        else: palindromic = testP
    
    return palindromic

        
"""
***************
Test Procedures
***************
Call testPalin(n) with the number of test cases required. If no error is
found, the function will return False. If an error is found, the function
will return True after first printing the value of the test variables:
    
    m = The greatest palindromic number less than n as calculated by
        the function getGreatestPalindromicNumber(n)
        
    n = The original number
    
    i = The palindromic number found in between the one chosen by
        getGreatestPalindromicNumber(n) and the original number.
"""        

def _testPalin(n):
    m = getGreatestPalindromicNumber(n)
    
    for i in range(m + 1, n):
        if isPalindromic(i):
            print(m, n, i)
            return True
    return False
    
def testPalin(n):
    import random
    faultFound = False
    for i in range(n):
        x = random.randint(100,999999)
        if _testPalin(x): faultFound = True
    print(faultFound)
    
def testPalin2(n):
    import random
    faultFound = False
    for i in range(n):
        x = random.randint(100,999)
        x = int(str(x) + str(x)[::-1])
        if _testPalin(x): faultFound = True
    print(faultFound)
        
