# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 13:11:07 2020

@author: b
"""
import Lab04_Module

outfile = open('unique_file.txt','w')
for i in range(1,4):
    file = open('words'+str(i)+'.txt','r')
    data = file.read()
    data = Lab04_Module.clean_data( data )
    unique,count = Lab04_Module.find_unique( data )
    outfile.write(unique+','+str(count)+'\n')

outfile.close()

uniques = Lab04_Module.count_uniques( 'unique_file.txt' )
print('Number of unique words in files:',uniques)