# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 11:27:05 2024.

q: A robot moves in a plane starting from the original point (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to
compute the distance from current position after a sequence of movement
and original point. If the distance is a float, then just print the nearest
integer.

ex:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

@author: doga
"""

from math import sqrt
def walk():
    print("here are the available commands:\n"
          "up [number]: go up by [number] amount (example use: up 7)\n"
          "down [number]: go down by [number] amount\n"
          "left [number]: go left by [number] amount\n"
          "right [number]: go right by [number] amount\nq: quit")
    position = [0, 0]
    while True:
        print(position)
        a = input("please select what you would like to do: ")
        b = []
        b = a.split(' ')
        if (b[0].lower() == 'up' or b[0].lower() == 'down' or 
            b[0].lower() == 'right' or b[0].lower() == 'left'):
            if b[0].lower() == 'up':
                position[1] += int(b[1])
            elif b[0].lower() == 'down':
                position[1] -= int(b[1])
            elif b[0].lower() == 'left':
                position[0] -= int(b[1])
            elif b[0].lower() == 'right':
                position[0] += int(b[1])
            else:
                print("how did you even get here??")
        elif a.lower() == 'q':
            print("bye~")
            return position
        else:
            print("hm?")
def distance(a):
    return sqrt(a[0]**2 + a[1]**2)
move = walk()
print(round(distance(move)))
