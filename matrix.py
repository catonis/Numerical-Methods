# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 02:15:27 2019

@author: Chris Mitchell

Getting a determinant by means of the Laplace Expansion.

"""

import numpy as np

def initMatrix():
    M = np.array([[ 3,  0,  0, -2,  4],
                  [ 0,  2,  0,  0,  0],
                  [ 0, -1,  0,  5, -3],
                  [-4,  0,  1,  0,  6],
                  [ 0, -1,  0,  3,  2]])
    return M

def getMinor(M, m, n):
    x, y = M.shape
    rowIndex = [i for i in range(x) if i != m]
    colIndex = [i for i in range(y) if i != n]
    return M[rowIndex,:][:,colIndex]

def getDeterminant(M):
    x, y = M.shape
    if x != y: raise Exception("The matrix must be square.")
    if x == 1: return M[0][0]
    else:
        det = 0
        cofactor = -1
        for i in range(x):
            cofactor = -cofactor
            minor = getMinor(M, 1, i)
            det = det + (cofactor * M[1,i] * getDeterminant(minor))
    return det

