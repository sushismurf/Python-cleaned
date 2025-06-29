# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:57:53 2023.

@author: billypatty

Take a list and return a list containing all the elements but their duplicates.
"""


def LdupRemover(k):
    """
    Remove the duplicates in a list.

    Parameters
    ----------
    k : list
        the list provided by user.

    Returns
    -------
    m : list
        the list k with duplicates removed.
    """
    m = []
    for i in k:
        if i not in m:
            m.append(i)
    return m


userList = []

while True:
    a = input("please enter something to add to the list (quitlist to stop): ")
    if a.lower() == 'quitlist':
        print("quitting list input...")
        break
    else:
        userList.append(a)

if len(userList) != 0:
    print("the original list:")
    print(userList)

    print("list after duplicates removed: ")
    print(LdupRemover(userList))
else:
    print("the list is empty, nothing to see here.")
