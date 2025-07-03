# -*- coding: utf-8 -*-
"""
Lab 3 q2
"""


def get_substring_positions(s1, s2):
    """
    returns the number of positions where s1 and s2 have the same 
    substring of length 2

    Parameters
    ----------
    s1 : str
        first string
    b : str
        second string

    Returns
    -------
    count : int
        number of positions of the substrings of length 2

    """
    min_length = min(len(s1), len(s2))
    count = 0
    for i in range(min_length-1):
        if s1[i:i+2] == s2[i:i+2]:
            count += 1
    return count

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

while str1 and str2:
    result = get_substring_positions(str1, str2)
    print('"' + str1 + '"','and', '"' + str2 + '"', 'have', result,'positions where they contain the same substrings of length 2')
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
   
    
            

