# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:15:29 2023.

@author: doga

Write a function is_in that accepts two strings as
arguments and returns True if either string occurs anywhere in the
other, and False otherwise.
"""


def is_in(string1, string2):
    """
    Define the function that states whether one of the stings is in the other.

    Parameters
    ----------
    string1 : string
        a string the user inputs.
    string2 : string
        another string the user inputs.

    Returns
    -------
    True or False.
    """
    if string1.lower() in string2.lower():
        return True
    elif string2.lower() in string1.lower():
        return True
    else:
        return False


def test_is_in(tstring1, tstring2):
    """
    Define a test function for is_in.

    Parameters
    ----------
    tstring1 : string
        a set of test words.
    tstring2 : string
        another set of test words.

    Returns
    -------
    None.
    """
    for i in tstring1:
        for j in tstring2:
            result = is_in(i, j)
            if result is not True or result is not False:
                print("oh no")
            else:
                print("okay it works.")


word1 = input("please input a word: ")
word2 = input("please input another word: ")

if is_in(word1, word2):
    print("yay")
else:
    print("nay")
