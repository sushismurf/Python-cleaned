# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 12:52:32 2023.

@author: doga

 Write a function that meets the specification
 def shopping_days(year):
 year a number >= 1941
 returns the number of days between U.S. Thanksgiving
and
 Christmas in year
"""

import datetime as cal


def find_thanksgiving(year):
    month = cal.monthcalendar(year, 11)
    if month[0][cal.THURSDAY] != 0:
        thanksgiving = month[3][cal.THURSDAY]
    else:
        thanksgiving = month[4][cal.THURSDAY]
        return thanksgiving

"""
def shopping_days(year):
    if year < 1941:
        return -1
    else:
        tgDate = find_thanksgiving(year)
        month = cal.monthcalendar(year, 11)
        chrDate = month[11][cal.]
        """
years = input("year: ")
print(find_thanksgiving(years))
