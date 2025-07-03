#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 17:53:20 2023

"""
from Employee import Employee

class Manager(Employee):
    
     def __init__(self, name, id_num, wage, bonus):
         super().__init__(name, id_num, wage)
         self.__bonus = float(bonus)
    
     def get_bonus(self):
         return self.__bonus
    
     def calculate_salary(self):
        salary = (self.get_wage() * 1.1 + self.__bonus)
        salary -= salary * Employee.tax_rate
        return salary

     def __repr__(self):
         emp = Employee.__repr__(self)
         emp += ' Bonus: '+str(self.get_bonus())
         return emp
        
