# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
def find_function( choice ):
    if choice == 1:
        return int
    elif choice == 2:
        return float
    else:
        return bool

value = input('Enter value: ')
print('Convert value to:')
choice = int( input('\t1 - int\n\t2 - float\n\t3 - bool\nchoice: '))
fcn = find_function( choice )
value = fcn( value )
print(f'Updated value {value} is type {type(value)}')

