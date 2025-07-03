# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 15:56:44 2023.

@author: doga
"""


def remove_adjacent_duplicates(input_string):
    """Define the function which removes adjacent duplicates."""
    result = []
    for char in input_string:
        if not result or char != result[-1]:
            result.append(char)
    return ''.join(result)


input_string = input("Enter a string: ")
output_string = remove_adjacent_duplicates(input_string)

print("String with adjacent duplicates removed:", output_string)
