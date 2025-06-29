# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:05:51 2024.

q: Assuming that we have some email addresses in the "username@companyname.com"
format, please write program to print the company name of a given email
address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

google

In case of input data being supplied to the question, it should be assumed
to be a console input.

@author: sushismurf
"""

a = input("give your mail: ")
while True:
    if '@' in a:
        b = str()
        for i in a:
            if i == '@':
                b += a[a.index(i)+1:a.rindex('.')]
                break
            else:
                pass
        break
    else:
        print("that doesn't really look like an email..")
    a = input("give your mail: ")
print(b)
