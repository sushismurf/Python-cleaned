# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:10:18 2024.

q: A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will
check them according to the above criteria. Passwords that match the criteria
are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

@author: doga
"""

def passCheck():
    lowerFlag = None
    upperFlag = None
    numberFlag = None
    idkFlag = None
    realPass = []
    while True:
        a = input("give a comma-separated sequence of passwords"
                  " (example: pass1,pass2): ")
        d = a.split(',')
        for i in d:
            for j in i:
                if j.isalpha() and j.islower():
                    lowerFlag = True
                elif j.isalpha() and j.isupper():
                    upperFlag = True
                elif j.isdigit():
                    numberFlag = True
                elif j in "$@#":
                    idkFlag = True
                else:
                    lowerFlag = None
                    upperFlag = None
                    numberFlag = None
                    idkFlag = None
                    break
            if (lowerFlag is True and upperFlag is True and
               numberFlag is True and idkFlag is True):
                realPass.append(i)
                lowerFlag = None
                upperFlag = None
                numberFlag = None
                idkFlag = None
            else:
                lowerFlag = None
                upperFlag = None
                numberFlag = None
                idkFlag = None
        return realPass
p = passCheck()
print(','.join(p))
