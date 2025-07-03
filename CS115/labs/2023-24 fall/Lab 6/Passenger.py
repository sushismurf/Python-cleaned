# -*- coding: utf-8 -*-
"""
@author: CS115
"""

class Passenger:
     
    def __init__( self, pname, psurname, seatNo, fare = 1000):
        self.__passengerName = pname
        self.__passengerSurname = psurname
        self.__seatNo = seatNo
        self.__fare = fare
    
    def getName( self ):
        return self.__passengerName
    
    def getSurname( self ):
        return self.__passengerSurname
    
    def getSeatNumber( self ):
        return self.__seatNumber
    
    def setFare( self, price):
        self.__fare = price
  
    def calculate_fare( self ):
        if self.__fare < 1000:
            return self.__fare * 1.05 
        return self.__fare
    
    def __str__( self ):
           rep = 'Passenger Name:\t' + self.__passengerSurname  + ' ' + self.__passengerName    
           rep += ' Seat: ' + self.__seatNo + '\n'
           return rep
    
    def __repr__( self ):
           rep = '(' + self.__passengerSurname + ' ' + self.__passengerName[0] + '.\t'
           rep += self.__seatNo + '\t' + str(self.calculate_fare()) + 'TL)\n'
           return rep
           