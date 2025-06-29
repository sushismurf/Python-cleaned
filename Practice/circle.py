"""Assignment 2.

Finds the area & perimeter of a circle with a given radius.

"""

radius = 1.50  # the radius in centimeters
pi = 3.1415
perimeter = 2*pi*radius
areaC = pi*radius**2

if radius > 0:
    # trying to avoid too many digits. 2 decimels should be enough.
    print(f'The area of the circle is {areaC:.2f} cm^2, \
and the perimeter is equal to {perimeter:.2f} centimeters.')

else:
    print('Radius must be greater than 0. Please input a valid number.')
