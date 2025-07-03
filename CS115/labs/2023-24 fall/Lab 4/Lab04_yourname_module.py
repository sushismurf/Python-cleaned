# -*- coding: utf-8 -*-
"""
@author: CS115
"""

def findAuthor(fn1, fn2):
    """
    finds the name of each author on each line in fn1
    and outputs just the author names to fn2
    
    Parameters:
        fn1: str
             file name of the input file
        fn2: str
             file name of the output file
    Returns:
        None

    """
    inp = open(fn1, 'r')
    out = open(fn2, 'w')
    for line in inp:
        pos = line.find('~')
        out.write(line[pos + 1:])
    inp.close()
    out.close()
        


def findAveragePrice(fn1, cityName, distance):
    """
    reads fn1 and returns the average price for only 
    the hotels in the cityName within given distance 
    to the city center.  

    Parameters
    ----------
    fn1 : str
        input file name
    cityName : str
        given city name
    distance : float
        given distance

    Returns
    -------
    avg: float
        average price 

    """
    inp = open(fn1, 'r')
    total = 0
    count = 0
    avg = None
    
    for line in inp:
        pos1 = line.find(';')
        city = line[:pos1]
        if city == cityName:
            pos2 = line.find(';', pos1 + 1)
            pos3 = line.rfind(';')
            dist = float(line[pos2 + 1: pos3])
            if dist <= distance:
                total += float(line[pos3 + 1:])
                count += 1
            
    if count != 0:
        avg = total / count
    
    inp.close()
    return avg
    
        




