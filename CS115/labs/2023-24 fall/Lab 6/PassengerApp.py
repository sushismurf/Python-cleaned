# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 12:47:07 2023

@author: user
"""
from Passenger import *
import random

def load_passengers( fname ):
    passengers = []
    my_file = open(fname, 'r') 
    for line in my_file:
        data = line.split(';')
        pname = data[0]
        psurname = data[1]
        fare = int( data[2] )
        seatNo = data[3].strip()
        
        passenger = Passenger( pname, psurname, seatNo, fare )
        passengers.append( passenger )
        
    my_file.close()
    return passengers


passenger_list = load_passengers( 'passengers.txt' )
name = input('Enter name: ')
surname = input('Enter surname: ')
found = False
       
for psgr in passenger_list:
    if psgr.getName() == name and psgr.getSurname() == surname:
        fare = int(input('Enter new price: '))
        psgr.setFare(fare)
        print(psgr, 'UPDATED')
        found = True
        break

if not found:
    print('Passenger is NOT Found!')         
   
print('\nPassenger List: ')
print(passenger_list)
