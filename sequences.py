# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 04:40:31 2019

@author: Chris Mitchell
"""

import requests
import re

def get_oeis_ref(sequence_ref):
    """This function accepts a sequence identification number as a string
       for the OEIS and pulls the sequence, name, and comment from the
       database in the JSON format. The function returns a list of
       integers containing the reference data."""

    #Sequence IDs are in the form of A123456
    #Use regular expressions to enforce proper format
    p = re.compile('^A\d{6}$')
    if p.findall(sequence_ref) == []:
        raise TypeError('Invalid sequence format.')
       
    #Set the appropriate url to query
    url = 'https://oeis.org/search?q=id:' + sequence_ref + '&fmt=json'
    
    #Make the request for the data
    req = requests.get(url)
    
    #Read the request as a JSON and unnest
    oeis_json = req.json()
    oeis_json = oeis_json['results'][0]
    
    #Break the 'data' field down into a list of numbers and return
    return [int(seq_val) for seq_val in oeis_json['data'].split(',')]
    
def collatzSequence(start):
    """Returns the Collatz sequence for the starting number as a list of
       integers."""
    
    evenFunc = lambda x : x // 2
    oddFunc = lambda x : (3 * x) + 1
    
    colList = [start]
    while start != 1:
        if start % 2 == 0:
            start = evenFunc(start)
        else:
            start = oddFunc(start)
        colList.append(start)
        
    return colList
        