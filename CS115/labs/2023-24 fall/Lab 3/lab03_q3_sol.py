# -*- coding: utf-8 -*-
"""
Lab 3 q3
"""
def getSuffix(num, size):
    """
    returns an integer value that is the suffix of 
    num having size digits
    
    Parameters
    ----------
    num : integer
          given number
    size: int 
          size of suffix
        
    Returns
    -------
    count: int
           suffix of num having size digits
    """

    divisor = 1
    
    for i in range(size):
        divisor = divisor * 10

    return num % divisor
	

def getNoOfDigits(n):
    """
    that takes n, and returns the number of digits 
    in n using getSuffix method (from part a above) 

    Parameters
    ----------
    n : integer
        given number
    Returns
    -------
    digits: int
            no of digits of n

    """
    digits = 1
    while n != getSuffix(n, digits):
        digits += 1
		
    return digits

    

for i in range(3):
    number = int(input('Enter an integer number: '))
    suf = int(input('Enter the number of digits of suffix: '))
    suffix = getSuffix(number, suf)
    print('The suffix is:', suffix)
    print('The number of digits of',number,'is', getNoOfDigits(number))
    