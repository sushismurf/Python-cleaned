"""Assignment 1.

Converts Kelvin to Celcius.

"""

valueK = 400  # the value to be converted (Kelvin)
valueC = valueK - 273

if valueK >= 0:
    print(f'{valueK} Kelvin is {valueC} degrees Celcius.')

if valueK < 0:
    print('Such a temperature does not exist. Please input a valid number.')
