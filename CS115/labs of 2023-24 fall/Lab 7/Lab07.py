#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 17:58:41 2023

"""

from Employee import *
from Manager import *

def read_employees(filename):
    emp_list = []
    emp_file = open(filename, 'r')
    for line in emp_file:
        data = line.strip().split(',')
        id_num = data[2]
        wage = data[3]
        name = data[1]
        if data[0] == 'E':
            emp = Employee(name, id_num, wage)
        elif data[0] == 'M':
            bonus = int(data[4])
            emp = Manager(name, id_num, wage, bonus)
        if emp not in emp_list:
            emp_list.append(emp)
        else:
            print('Duplicate employee id:', emp)
            print('not added')
            
    emp_file.close()
    return emp_list

# read the employees from the input file    
emp_list = read_employees('employees.txt')

# sort the list and display the sorted list
emp_list.sort()
print('\nSorted List: ')
print(emp_list)

# display the salary of all employees
total = 0
count = 0
print('\nSalary of all employees:')
for emp in emp_list:
    print(emp.get_emp_name(),'salary after tax:',emp.calculate_salary())
    if isinstance(emp, Manager):
        total += emp.calculate_salary()
        count += 1

print('\nAverage Salary for Managers:', total/count)
                