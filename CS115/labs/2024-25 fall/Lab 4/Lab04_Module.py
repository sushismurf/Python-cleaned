# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:23:45 2020

@author: b
"""
def clean_data( data ):
    data = data.replace('\n',' ')
    data = data.lower()
    data = data.replace('.','')
    data = data.replace('?','')
    data = data.replace(',','')
    return data

def find_unique( data ):
    s_ind = 0
    e_ind = 0
    unique = ''
    count = 0
    
    while e_ind != -1:
        e_ind = data.find(' ', s_ind+1)
        word = data[s_ind:e_ind]
   
        if data.count(word) == 1:
            unique += word+' '
            count += 1
        s_ind = e_ind+1
    return (unique, count)

def count_uniques( fname ):
    file = open(fname, 'r')
    count = 0
    for line in file:
        pos = line.rfind(',')
        count += int(line[pos + 1:])
    return count


