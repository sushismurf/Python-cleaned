#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:06:22 2024

"""

birth_date = input('Enter date of birth: ')
day = int(birth_date[:2])
month = int(birth_date[3:])

current_month = 9
current_date = 30

if month < current_month:
    print('Birthday passed')
elif month > current_month:
    months = month - current_month
    print(months,'months until birthday')
else:
    days = day - current_date
    if days >= 0:
        print(days,'days until the birthday')
    else:
        print('Birthday passed')
