# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 11:27:34 2020

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np

c_names = np.loadtxt('c_names.txt', skiprows=1, dtype='str')
data = np.loadtxt('c_data.txt', skiprows=1)

#get data for countries with female fertility rate under 3
under_3 = data[:,0] < 3
fertility_under_3 = data[under_3]

#suppresses scientific/exponential notation
np.set_printoptions(suppress=True)

# #get data for countries in Asia
asia = c_names[:,1] == 'Asia'
asian_countries = c_names[asia]
asia_data = data[asia]


plt.figure(1)
plt.clf()

plt.subplot(2,2,1)
plt.plot(data[:,6], 100-data[:,10], 'b*--')
plt.xlabel('GDP')
plt.ylabel('Female Literacy Rate')
plt.title('Female Literacy vs GDP')

plt.subplot(2,2,2)
bar_width = 0.25
plt.bar( 'Fertility Below 3', np.mean(fertility_under_3[:,5]))
plt.bar( 'All Fertility', np.mean(data[:,5]))
plt.ylabel('Infant Mortality')
plt.title('Comparison of Average Infant Mortality')


plt.subplot(2,2,3)
plt.title('Employment Rates by Gender in Asia')

labels = ('Male', 'Female')
explode = (0, 0.1)
plt.pie([np.mean( asia_data[:,7]),np.mean( asia_data[:,8])] ,labels=labels,autopct='%1.1f%%', explode = explode)


plt.subplot(2,2,4)
plt.title('Frequency of GDP for All Countries (4 bins)')

res = plt.hist(data[:,6],4)
plt.xticks( res[1] )

plt.figure(2)
plt.clf()
plt.plot(asian_countries[:,0], asia_data[:,6],   'b*')
plt.xticks(rotation = 45)
plt.ylabel('GDP per capita')
plt.title('Per Capita GDP - Asian Countries')


