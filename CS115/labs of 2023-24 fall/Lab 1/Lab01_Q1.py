#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 14:48:16 2023

"""

TIP = 0.15
TAX = 0.08
mealAmount = float(input("Enter meal amount(in dollars): "))
taxAmount = mealAmount * TAX
tipAmount = mealAmount * TIP

total = mealAmount + taxAmount + tipAmount
		
print("Meal: $",mealAmount)
print("Tip Amount: $", tipAmount)
print("Sales Tax: $", taxAmount)
print("Total: $", total)