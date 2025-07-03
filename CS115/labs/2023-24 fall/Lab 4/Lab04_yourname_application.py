# -*- coding: utf-8 -*-
"""
@author: CS115
"""

import Lab04_yourname_module as md

md.findAuthor('quotes.txt','authors.txt')

city = input('Enter city to search: ')
distance = float(input('Enter maximum distance from city center (kms): '))

averagePrice = md.findAveragePrice('restaurants.txt', city, distance)

if averagePrice != None:
    print('Average price of hotels less than', distance, 'km from the city center of', city, 'is: ', averagePrice,'TL')
else:
    print('No restaurant is Found in the the given distance for the given city')
    
    