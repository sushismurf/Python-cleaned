# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:45:12 2023.

@author: doga

Using functions, ask the user for a long string containing multiple words.
Print back the same string, except with the words in backwards order.
"""


def sentenceFlipper(a):
    """
    Take a string and reverse the word order.

    Parameters
    ----------
    a : str
        whatever the user has input.

    Returns
    -------
    b : str
        a, but words reversed.
    """
    b = a.split(' ')
    flipList = list(b)
    c = []
    for i in range(len(flipList) - 1):
        c.append(b[-(i+1)])
    c.append(b[0])
    return c


userS = input("please enter a sentence: ")
sFlipped = sentenceFlipper(userS)

print("the sentence with words in reverse order is:")

for j in range(len(sFlipped)):
    print(sFlipped[j], end=' ')
