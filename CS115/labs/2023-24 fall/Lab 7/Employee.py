#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 16:42:22 2023

"""

class Employee(object):
    tax_rate = 0.3
    
    def __init__(self, name, id_num, wage):
        self.set_emp_name(name)
        self.set_id_num(id_num)
        self.set_wage(wage)
        
    def get_emp_name(self):
        return self.__emp_name
    
    def set_emp_name(self, new_name):
        name = ''
        for ch in new_name:
            if ch.isalpha() or ch == ' ':
                name += ch
                
        self.__emp_name = name 
    
    def get_id_num(self):
        return self.__id_num
    
    def set_id_num(self, new_num):
        try:
            self.__id_num = int(new_num)
        except:
            self.__id_num = 11111111
    
    def get_wage(self):
        return self.__wage
    
    def set_wage(self, new_wage):
        new_wage = float(new_wage)
        if new_wage > 0:
            self.__wage = new_wage
        else:
            self.__wage = 0
    
    def calculate_salary(self):
       salary = self.__wage - self.__wage * Employee.tax_rate
       return salary
   
    def __lt__(self, other):
        self_pos = self.__emp_name.rfind(' ')
        other_pos = other.__emp_name.rfind(' ')
        self_surname = self.__emp_name[self_pos+1:]
        other_surname = other.__emp_name[other_pos+1:]
        self_name = self.__emp_name[:self_pos]
        other_name = other.__emp_name[:other_pos]
        
        if self_surname < other_surname:
            return True
        elif self_surname > other_surname:
            return False
        else:
            return self_name < other_name
        
    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.__id_num == other.__id_num
        return False
    
    def __repr__(self):
        return f'\nName: {self.__emp_name} \
            Employee ID: {self.__id_num} Wage: {self.__wage}'
    
