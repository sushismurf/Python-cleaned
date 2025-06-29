# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 11:23:21 2018

@author: b
"""
from datetime import *
class Member:
    __monthlyFee = 350
    
    def __init__(self, name, surname, memberId, year):
        self.__name = name;
        self.__surname = surname;
        self.__memberId = int(memberId);
        self.__birthYear = int(year);
    
    def getAge(self):
        year = datetime.now().year
        return year - self.__birthYear
    
    def getName(self):
        return self.__name

    def getSurname(self):
        return self.__surname

    def getMemberId(self):
        return self.__memberId

    def setSurname(self, surname):
        self.__surname = surname
    
    def calculateFee(self):
        if self.getAge() > 60:
            return (Member.__monthlyFee) * 0.7
        return Member.__monthlyFee
    
    def __repr__(self):
        outStr = "Member Id: "+str(self.__memberId)+" "
        outStr += "Name: "+self.__surname+","+self.__name+"\t "
        outStr += "Age: "+str(self.getAge())+"\t"
        outStr += "Fee: {0:.2f}".format(self.calculateFee())
        return outStr
    
    def __eq__(self, other):
        if isinstance(other, Member):
            if self.__memberId == other.__memberId:
                return True
        return False
    
    def __lt__(self, other):
        if self.__memberId < other.__memberId:
            return True
        return False
        
        
        
      