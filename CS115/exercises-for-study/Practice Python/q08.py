# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 09:56:05 2023.

@author: billypatty

Rock-Paper-Scissors game against computer.
"""

import random

comPick = ["rock", "paper", "scisors"]
comPoints = 0
userPoints = 0

print("Rock-Paper-Scisors!")

while True:
    userPick = input("rock, paper or scisors? (q to quit): ").lower()
    if userPick in comPick:
        comTurn = random.choice(comPick)
        print("the computer chose", comTurn)
        if userPick == 'rock':
            if comTurn == 'rock':
                continue
            elif comTurn == 'paper':
                comPoints += 1
            else:
                userPoints += 1
        if userPick == 'paper':
            if comTurn == 'rock':
                userPoints += 1
            elif comTurn == 'paper':
                continue
            else:
                comPoints += 1
        if userPick == 'scisors':
            if comTurn == 'rock':
                comPoints += 1
            elif comTurn == 'paper':
                userPoints += 1
            else:
                continue
    elif userPick == 'q':
        print("ending...")
        break
    else:
        print("that's not in the game...")
        break
    print("player", userPoints, "-", comPoints, "computer")

if userPoints > comPoints:
    print("you win!")
elif userPoints == comPoints:
    print("it is a draw!")
else:
    print("you lost... better luck next time!")
