#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 14:52:19 2024

"""

import datetime
from Inpatient import *

def registerPatients(fileName, pList):
    inFile = open(fileName, 'r')
    for line in inFile:
        data = line.strip().split(';')
        name = data[0] 
        aDate = data[1]
        ins = data[2] == 'True'
 
        if ins:
            coverage = float(data[3])    		
            p = Inpatient( name,  ins, aDate, coverage/100 )
        else:
            p = Inpatient(name, ins, aDate )
        pList.append(p)    	
    inFile.close()
    
def dischargePatients( fileName, pList):
    inFile = open(fileName,'r')
    for line in inFile:
        data = line.strip().split(';')
        name = data[0] 
        dDate = data[1]
        for patient in pList:
            if patient.getPName().lower() == name.lower():
                patient.setDischargeDate(dDate)    	
    inFile.close()
		
        
pList = []
registerPatients("patients.txt", pList)
dischargePatients("discharge.txt", pList)
print(pList)
