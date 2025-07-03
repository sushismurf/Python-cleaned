"""
Created on Thu Oct 12 00:16:54 2023.

@author: doga
Write a Python script, Lab01_Q1.py that inputs 3 decimal numbers, a, b
and c from the user. Calculate the result of the following equation and
display the result. The output should be formatted the same as the
sample run below.
"""

numA = int(input("input a: "))
numB = int(input("input b: "))
numC = int(input("input c: "))

valueR = (numA * numB + numA * numC + numB * numC) / numA + numB + numC

print(f"the result is {valueR:.2f}")
