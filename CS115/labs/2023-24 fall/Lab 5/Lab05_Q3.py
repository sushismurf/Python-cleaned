#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:44:05 2023

"""

def addCustomer(customers, key, value):
    if key not in customers:
        customers[key] = []
        customers[key].append(value)
        print('Customer Added')
    else:
        print('Customer already exists')
        
def addAccount(customers,key, value):
    if key in customers:
        customers[key].append(value)
    else:
        print('Customer not found')
        
def findCustomer(customers,key):
    if key in customers:
        return customers[key]
    else:
        print('Customer does not exist')
        return None
        
customers = {}
choice = int(input('1)Add Customer\n2)Search Customer\n3)Add Account\n4)Quit\nEnter Choice: '))
while choice != 4:
    
    if choice == 1:
        customerNo = input('Enter customer number: ')
        account = int(input('Enter account id: '))
        branch = input('Enter branch name: ')
        balance = float(input('Enter balance: '))
        addCustomer(customers,customerNo, (account, branch, balance))
        
    elif choice == 2:
        customerNo = input('Enter customer number: ')
        customer = findCustomer(customers,customerNo)
        if customer != None:
            print("List of accounts:",customer)
    elif choice == 3:
        customerNo = input('Enter customer number: ')
        account = int(input('Enter account id: '))
        branch = input('Enter branch name: ')
        balance = float(input('Enter balance: '))
        addAccount(customers,customerNo, (account, branch, balance))
    else:
        print('Invalid choice')

    choice = int(input('1)Add Customer\n2)Search Customer\n3)Add Account\n4)Quit\nEnter Choice: '))
print('Program Ended....')

