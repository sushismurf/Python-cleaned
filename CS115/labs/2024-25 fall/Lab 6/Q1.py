# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:56:27 2022

@author: user
"""
def printMatrix(m):
    """
    display m in matrix form
    """
    for row in range(len(m)):
        for col in range (len(m[row])):
            print(f'{m[row][col]:2d}',end = ' ')
        print()
   
def formMatrix(n):
    """
    stores the sum of row and column indices into
    upper triangular part of m and absolute value 
    of the difference of row and column indices 
    into lower triangular part of m and 0 to the diagonal.
    
    Parameters:
    -----------
    n: int
       no of rows and columns
            
    Returns
    ----------
    m: matrix
       of integer values
    
    """
    m = []
    
    for r in range(n):
        row = []
        for c in range (n):
            if r % 2 == 0 and c % 2 == 0:
                row.append(r)
            elif r % 2 == 1 and c % 2 == 1:
                row.append(c)
            else:
                row.append(0)
        m.append(row)
                
    return m

n = int(input('Enter size of the matrix: '))
mat = formMatrix(n)
printMatrix(mat)


