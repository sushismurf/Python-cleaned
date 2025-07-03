# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:27:39 2023.

@author: doga

Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right.
"""

import random

allowedNums = range(1, 10)
someNumber = random.choice(allowedNums)
totalGuesses = 0

print("number guessing game!")

while True:
    userGuess = input("guess a number [1, 9]: ")
    totalGuesses += 1
    try:
        userGuess = int(userGuess)
        if userGuess == someNumber:
            print("you guesssed it right!")
            print("it took you", totalGuesses, "guesses.")
            keepGo = input("another round? (y or n): ").lower()
            if keepGo == 'y':
                someNumber = random.choice(allowedNums)
                totalGuesses = 0
                continue
            else:
                print("well, see you next time!")
                break
        elif userGuess > someNumber:
            print("you need something lower than that...")
        if userGuess < someNumber:
            print("you need something greater than that...")
    except ValueError:
        print("that is not an integer...")
        break
