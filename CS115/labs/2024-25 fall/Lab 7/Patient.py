#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:29:23 2024

"""


class Patient:
    __hospitalFee = 1000
    
    def __init__( self, name,  ins,  cPercent=0.0):
        self.__pName = name
        self.__isInsured = bool(ins)
        self.setCoveragePercent(float(cPercent))
    
    def getPName(self):
        return self.__pName
    
    def setPName( self,name):
        self.__pName = name

    def getHospitalFee():
        return Patient.__hospitalFee
      
    def isInsured(self):
        return self.__isInsured
    
    def setIsInsured( self, insured):
        self.__isInsured = insured
    
    def getCoveragePercent(self):
        return self.__coveragePercent
    
    def setCoveragePercent( self,cPercent):
        if cPercent > 0 :
            self.__coveragePercent = cPercent 
    
    def calculateFee(self):
        if self.__isInsured: 
            return Patient.__hospitalFee - Patient.__hospitalFee * self.__coveragePercent
        else:
            return Patient.__hospitalFee
    
    def __repr__(self):
        data = '\nPatient Name: '+self.__pName+' Insurance: '
        if self.__isInsured:
            data += '(yes)'
        else:
            data += '(no)' 
        data += '\n'
        return data
