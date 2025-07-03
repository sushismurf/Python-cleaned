# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:33:39 2024.

q: Write a program that computes the net amount of a bank account based a
transaction log from console input. The transaction log format is shown as
following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

@author: doga
"""

balance = 0
print("welcome.\nfor help, type 'h'.\nto quit, type 'q'.")
while True:
    i = input("what would you like to do?: ")
    if i.lower() == 'h':
        print("this is the help screen.\ntype d [amount] to deposit "
              "said amount of money. ex: d 100\ntype w [amount] to "
              "withdraw said amount of money. ex: w 200\ntype q "
              "to quit anytime, saving the changes you've made.")
    elif i[0].lower() == 'd' and i[1] == ' ':
        balance += int(i[2:])
        print("deposited", i[2:], "to your account.\ncurrent balance is " +
              str(balance) + ".")
    elif i[0].lower() == 'w' and i[1] == ' ':
        balance -= int(i[2:])
        print("withdrawed", i[2:], "from your account.\ncurrent balance is " +
              str(balance) + ".")
    elif i[0].lower() == 'q':
        print("have a nice day.")
        break
    else:
        print('hm?')
