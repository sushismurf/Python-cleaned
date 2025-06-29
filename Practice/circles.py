# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 11:35:23 2025

@author: sushismurf
"""

from sympy import Eq, symbols, solve
import numpy as np


def dimension():
    """
    determines what dimension we'll deal with depending on user input.

    Returns
    -------
    the dimension in int

    """
    while True:
        a2or3 = input("is your circle in 2D or 3D?: ")
        try:
            a2or3 = int(a2or3)
            if a2or3 == 2:
                return 2
            elif a2or3 == 3:
                return 3
            else:
                print("That is not an acceptable dimension. Please enter either 2 or 3.")
        except:
            print("are we sure that's an integer?")


def points(d):
    if d == 2:
        p1 = []
        p2 = []
        p3 = []
        while True:
            x = input("please give the x value for P1: ")
            y = input("please give the y value for P1: ")
            try:
                x = float(x)
                y = float(y)
                p1.append(x)
                p1.append(y)
                break
            except:
                print("invalid input. give integer or float for each value")
        while True:
            x = input("please give the x value for P2: ")
            y = input("please give the y value for P2: ")
            try:
                x = float(x)
                y = float(y)
                p2.append(x)
                p2.append(y)
                break
            except:
                print("invalid input. give integer or float for each value")
        while True:
            x = input("please give the x value for P3: ")
            y = input("please give the y value for P3: ")
            try:
                x = float(x)
                y = float(y)
                p3.append(x)
                p3.append(y)
                break
            except:
                print("invalid input. give integer or float for each value")
        equation2D(p1, p2, p3)

    else:
        p1 = []
        p2 = []
        p3 = []
        while True:
            x = input("please give the x value for P1: ")
            y = input("please give the y value for P1: ")
            z = input("please give the z value for P1: ")
            try:
                x = float(x)
                y = float(y)
                z = float(z)
                p1.append(x)
                p1.append(y)
                p1.append(z)
                break
            except:
                print("invalid input. give integer or float for each value")
        while True:
            x = input("please give the x value for P2: ")
            y = input("please give the y value for P2: ")
            z = input("please give the z value for P2: ")
            try:
                x = float(x)
                y = float(y)
                z = float(z)
                p2.append(x)
                p2.append(y)
                p2.append(z)
                break
            except:
                print("invalid input. give integer or float for each value")
        while True:
            x = input("please give the x value for P3: ")
            y = input("please give the y value for P3: ")
            z = input("please give the z value for P3: ")
            try:
                x = float(x)
                y = float(y)
                z = float(z)
                p3.append(x)
                p3.append(y)
                p3.append(z)
                break
            except:
                print("invalid input. give integer or float for each value")
        v1 = [p1[0]-p2[0],p1[1]-p2[1],p1[2]-p2[2]]
        v2 = [p2[0]-p3[0],p2[1]-p3[1],p2[2]-p3[2]]
        n = np.cross(v1, v2)
        n = n.tolist()
        equation3D(p1, p2, p3, n)


def equation2D(P_1, P_2, P_3):
    """
    the general form should be:
        (x-x_0)**2 + (y-y_0)**2 = r**2
    there are three points coming from the other function so just solve.

    Returns
    -------
    a unique equation in 2D

    """
    x_0, y_0, r = symbols('x_0 y_0 r')
    eq1 = Eq((P_1[0]-x_0)**2 + (P_1[1]-y_0)**2, r**2)
    eq2 = Eq((P_2[0]-x_0)**2 + (P_2[1]-y_0)**2, r**2)
    eq3 = Eq((P_3[0]-x_0)**2 + (P_3[1]-y_0)**2, r**2)
    solution = solve((eq1, eq2, eq3), (x_0, y_0, r))
    if any(val == x_0 or val == y_0 or val == r for val in solution[0]):
        print("points are linear!")
        result = -1
    else:
        print("here is the equation for that circle: ")
        print(f"(x-({solution[0][0]}))**2 + (y-({solution[0][1]}))**2 = ({solution[0][2]})**2")
        return 1


def equation3D(P_1, P_2, P_3, n):
    """
    similar but this time there is z too, so:
        (x-x_0)**2 + (y-y_0)**2 + (z-z_0)**2 = r**2
    also somehow we have to define the plane equation:
        n_x*(x-x_0)**2 + n_y*(y-y_0)**2 + n_z*(z-z_0)**2 = 0
    inserting a random point should work. so P_3 it is.

    Returns
    -------
    a unique equation in 3D

    """
    x_0, y_0, z_0, r = symbols('x_0 y_0 z_0 r')
    eq1 = Eq((P_1[0]-x_0)**2 + (P_1[1]-y_0)**2 + (P_1[2]-z_0)**2, r**2)
    eq2 = Eq((P_2[0]-x_0)**2 + (P_2[1]-y_0)**2 + (P_2[2]-z_0)**2, r**2)
    eq3 = Eq((P_3[0]-x_0)**2 + (P_3[1]-y_0)**2 + (P_3[2]-z_0)**2, r**2)
    eq4 = Eq(n[0]*(P_3[0]-x_0)**2 + n[1]*(P_3[1]-y_0)**2 + n[2]*(P_3[2]-z_0)**2, 0)
    solution = solve((eq1, eq2, eq3, eq4), (x_0, y_0, z_0, r))
    if np.linalg.norm(n) < 1e-8:
        print("points are linear!")
        result = -1
    else:
        print("here is the equation for that circle: ")
        print(f"(x-({solution[0][0]}))**2 + (y-({solution[0][1]}))**2 + (z-({solution[0][2]}))**2 = ({solution[0][3]})**2")
        return 1


if __name__ == "__main__":
    d = dimension()
    points(d)