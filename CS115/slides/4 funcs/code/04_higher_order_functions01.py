# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
import math

def do_this( num, this ):
    return this(num)

val = float(input('Enter a number: '))

#do this - find the ceiling of the value 
result = do_this(val,math.ceil)
print(f'Ceiling  of {val} is {result}')

#do this - find the int representation of the value
result = do_this(val,int)
print(f'int representation of {val} is {result}')

#do this - find the square root of the value
result = do_this( val, math.sqrt)
print(f'Rounded square root of {val} is {do_this(result,round)}')
