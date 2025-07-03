#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime

def get_birth(s):
    b_pos = s.find('(')
    d_pos = s.find('-')
    
    birth_year = s[b_pos + 1:d_pos]
    return int(birth_year)
 
def get_death(s):
    d_pos = s.find('-')
    p_pos = s.rfind(')')
    death_year = s[d_pos + 1:p_pos]
    if death_year:
        return int(death_year)
    return datetime.datetime.now().year

def get_age( s ):
    age = get_death(s) - get_birth(s)
    return age

def get_name(s):
    b_pos = s.find('(')
    composer_name = s[0:b_pos]
     
    return composer_name


#input a string containing a composer's name(birth_year-death_year)
composer_info = input('Enter composer information: ')

#store the name, birth_year and death_year in separate variables
name = get_name(composer_info)

age = get_age(composer_info)

print(name+"'s age: ",age)
 

