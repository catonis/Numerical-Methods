# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 03:24:57 2020

@author: Chris Mitchell
"""

def ulamSpiral(number, reverse = False):
    """Generates a two-dimensional list of size number by number + 1 which
       whose values form an Ulam Spiral. If reverse is false, the spiral runs
       counter-clockwise. If true, the spiral runs clockwise."""
    
    spiral = [[0 for i in range(number + 2)] for i in range(number + 2)]
    x = y = (number // 2) + 1
    counter = 1
    while counter < (number * number) + 1:
        spiral[x][y] = counter
        north = x - 1
        south = x + 1
        east = y + 1
        west = y - 1
        if spiral[north][y] == 0 and \
           spiral[south][y] == 0 and \
           spiral[x][east] == 0 and \
           spiral[x][west] == 0:
            y = east
        elif spiral[north][y] == 0 and \
             spiral[south][y] == 0 and \
             spiral[x][east] == 0 and \
             spiral[x][west] != 0:
            x = north
        elif spiral[north][y] == 0 and \
             spiral[south][y] != 0 and \
             spiral[x][east] == 0 and \
             spiral[x][west] == 0:
            y = west
        elif spiral[north][y] == 0 and \
             spiral[south][y] != 0 and \
             spiral[x][east] != 0 and \
             spiral[x][west] == 0:
            y = west
        elif spiral[north][y] == 0 and \
             spiral[south][y] == 0 and \
             spiral[x][east] != 0 and \
             spiral[x][west] == 0:
            x = south
        elif spiral[north][y] != 0 and \
             spiral[south][y] == 0 and \
             spiral[x][east] != 0 and \
             spiral[x][west] == 0:
            x = south
        elif spiral[north][y] != 0 and \
             spiral[south][y] == 0 and \
             spiral[x][east] == 0 and \
             spiral[x][west] == 0:
            y = east
        elif spiral[north][y] != 0 and \
             spiral[south][y] == 0 and \
             spiral[x][east] == 0 and \
             spiral[x][west] != 0:
            y = east
        elif spiral[north][y] == 0 and \
             spiral[south][y] != 0 and \
             spiral[x][east] == 0 and \
             spiral[x][west] != 0:
            x = north
        counter += 1
        
    spiral = spiral[1:number + 1]
    for row in spiral:
       row.pop(0)
       row.pop()
    if reverse:
        spiral = spiral[::-1]
    return spiral

def printUlamSpiral(spiral):
    
    x = len(str(max(spiral[len(spiral) // 2])))
    formatPiece = '{:' + str(x) + 'd} '
    formatStr = formatPiece * len(spiral[-1])
    for row in spiral:
        print(formatStr.format(*[row[i] for i in range(len(row))]))
        
def countUlamDiagonal(spiral):
    
    total = 0
    for i in range(len(spiral)):
        total += spiral[i][i]
        total += spiral[i][len(spiral) - 1 - i]
    #We counted the center '1' twice.
    total -= 1
    print(total)
    
    