# -*- coding: utf-8 -*-
"""
Created on Nov. 23  10:23:43 2022
@author: CS115
"""

from Birthday import *

def read_birthdays(filename):
    file = open(filename, 'r')
    birthdays = []
    for line in file:
        line = line.strip()
        data = line.split(';')
        bDay = Birthday(data[0],int(data[1]),int(data[2]))
        if bDay not in birthdays:
            birthdays.append(bDay)
        else:
            print(bDay.getName(),'is already in the list')
    return birthdays

def selection_sort(birthdays):
    suffixStart = 0
    while suffixStart != len(birthdays):
        for i in range(suffixStart, len(birthdays)):
            if birthdays[i] < birthdays[suffixStart]:
                birthdays[suffixStart], birthdays[i] = birthdays[i], birthdays[suffixStart]
        suffixStart += 1
        
def linearSearch(birthdays, month, day):
    names = []
    for i in range(len(birthdays)):
        if birthdays[i].getMonth() == month and birthdays[i].getDay() == day:
            names.append(birthdays[i].getName())
    return names
        

def binary_search(birthdays, name):  
    first = 0
    last = len(birthdays) - 1
    
    if first <= last:
        mid = (first + last)//2
        #if name is less than mid person's name
        if birthdays[mid].getName().lower() < name.lower():
            return(binary_search(birthdays[mid + 1:], name))
        elif birthdays[mid].getName().lower() > name.lower():
            return(binary_search(birthdays[:mid], name))
        else:
            return birthdays[mid]
                
 
#read the words into a list
bDays = read_birthdays('birthdays.txt' )
m = int(input('Enter the month: '))
d = int(input('Enter the day: '))
people = linearSearch(bDays, m, d)
if len(people) != 0:
    print('People Born on the given day:', people)
else:
    print('No birthday on that Day!')

#sort Birthdays by name
selection_sort(bDays)
print('Sorted List')
print(bDays)

name = input('Enter a name to search: ') 
    
person = binary_search(bDays, name)
print(person)
