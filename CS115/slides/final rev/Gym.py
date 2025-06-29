# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 11:27:20 2018

@author: b
"""

class Gym:
    
    def __init__(self, gymName):
        self.__members = []
        self.__branches = {}
        self.__gymName = gymName
    
    def addMember(self, member):
        if member not in self.__members:
            self.__members.append(member)
        else:
            print('**Duplicate Member(',member.getMemberId(),')**\n')

    def updateMemberSurname(self, memberId, surname):
        m = self.findMemberById(memberId)
        if m != None:
            m.setSurname(surname)
        else:
            print('Member not found')
        
    def sortMembers(self):
        self.__members.sort()
       
    def removeMember(self, searchId):
        try:
            m  = self.findMemberById(searchId)
            self.__members.remove(m)
        except:
            print('Member with given id does not exist')
     
    def findMemberById(self, sId):
        first = 0
        last = len(self.__members)-1
        mid = (first + last)//2
        while first <= last:
            mid = (first + last)//2
            if sId < self.__members[mid].getMemberId():
                last = mid -1
            elif sId > self.__members[mid].getMemberId():
                first = mid + 1
            else:
                return self.__members[mid]
        return None

    """def findMemberById(self, searchId):
        for m in self.__members:
            if m.getMemberId() == searchId:
                return m
        #function returns None if member not found
    """
    def addBranch(self, locName, city, phone):
        self.__branches[locName] = [city, phone]
    
    def findBranchInfo(self, branch):
        try:
            return self.__branches[branch]
        except:
            print('Branch not found')
            return None
        
    def getMemberAges(self):
        ageList = []
        for i in self.__members:
            ageList.append(i.getAge())
        return ageList
   
    def __repr__(self):
        gymStr = self.__gymName+'\n'
        gymStr += 'Branches:\n'
        for key in self.__branches:
            gymStr += key+'\n'
            
        gymStr += '\nMember List:\n'
        
        for m in self.__members:
            gymStr += str(m)+'\n'
        
        return gymStr
            
        
                 