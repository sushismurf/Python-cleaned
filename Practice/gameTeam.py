"""
Created on Thu Oct 12 00:23:51 2023.

@author: billypatty

Write a Python script, Lab01_Q2.py to request the name of a basketball
team, the number of games won, and the number of games lost as input,
and then display the name of the team and the percentage of games won.
Use format statement in the output.
"""

gameTeam = input("tell the name of the team: ")
gameWin = int(input("how many games did they win?: "))
gameLost = int(input("how many games did they lose?: "))
winRate = gameWin / (gameLost + gameWin) * 100

print(f"{gameTeam} won %{winRate:.1f} of their games.")
