# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:13:10 2023.

@author: billypatty
"""

mass = float(input("enter your weight (in kg): "))
height = float(input("enter your height (in m): "))
bmi = mass / height ** 2
idealweight = 22 * height ** 2

if bmi >= 24.9:
    print(f"your bmi is {bmi:.2f}.")
    print("you are overweight.")
    print(f"you should be around {idealweight:.1f} kg.")
elif bmi <= 18.5:
    print(f"your bmi is {bmi:.2f}.")
    print("you are underweight.")
    print(f"you should be around {idealweight:.1f} kg.")
else:
    print("your bmi is", bmi)
    print("your weight is normal. Keep up the healthy lifestyle!")
