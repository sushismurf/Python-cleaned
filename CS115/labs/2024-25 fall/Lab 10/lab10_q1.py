# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:36:29 2022

@author: user
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('economic_data.txt', delimiter=',')

x = data[:,4]
y = data[:,-1]


fit = np.polyfit(x, y, 1)
fit_y = np.polyval(fit, x)
    
plt.figure(1)
plt.clf()

plt.plot( x, y, 'ro')
plt.plot( x, fit_y, 'g--')
plt.xlabel('population')
plt.ylabel('employment rate')
plt.title('Relationship between employment rate and population')

