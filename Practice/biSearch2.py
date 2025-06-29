# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:02:31 2023.

@author: billypatty

trying to write bisection search myself.
"""

userNumber = int(input("please input a positive integer: "))
answerRoot = 0
answerLow = min(-1, userNumber)
answerHigh = max(1, userNumber)

if userNumber <= 0:
    print("that aint positive.")
else:
    while abs(answerRoot ** 2 - userNumber) >= 0.01:
        if answerRoot ** 2 > userNumber:
            answerHigh = answerRoot
        elif answerRoot ** 2 < userNumber:
            answerLow = answerRoot
        else:
            print(f"the square of {answerRoot} is approximately {userNumber}.")
        answerRoot = (answerHigh + answerLow) / 2

    print(f"the square of {answerRoot:.4f} is approximately {userNumber}.")
