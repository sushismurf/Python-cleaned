#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 14:20:18 2024

"""


from Patient import *
import datetime

class Inpatient(Patient):
    
    def __init__( self, name,  ins, aDate,cPercent= 0.0):
        Patient.__init__(self, name, ins, cPercent)
        self.setAdmitDate(aDate)
        self.__dischargeDate = None

    def getAdmitDate(self):
        return self.__admitDate
    
    def setAdmitDate( self,aDate):
        self.__admitDate = datetime.datetime.strptime(aDate, '%Y%m%d').date()
    
    def getDischargeDate(self):
        return self.__dischargeDate
    
    def setDischargeDate( self,dDate):
        self.__dischargeDate = datetime.datetime.strptime(dDate, '%Y%m%d').date() 
    
    def calculateFee(self):
        if self.__dischargeDate != None:
            daysStay = (self.__dischargeDate - self.__admitDate).days
            price = daysStay * Patient.getHospitalFee()
            if self.isInsured(): 
                return price - price * self.getCoveragePercent()
            else:
                return price
        return 0.0
        
    def __repr__(self):
            data = Patient.__repr__(self)
            data +='Admit Date: '+str(self.__admitDate)
            if self.__dischargeDate != None:
                data += '\nDischarged: '+str(self.__dischargeDate)
                data += '\n'
                data += 'Patient Balance: '+str(self.calculateFee())+'\n' 
            data += '\n'
            return data