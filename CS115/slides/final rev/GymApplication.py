# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 11:27:26 2018

@author: b
"""
from Member import *
from Gym import *
from matplotlib.pyplot import *
import matplotlib


inFile1 = open('gym_data.txt', 'r')
gymName = inFile1.readline().strip()
gym = Gym(gymName)
for line in inFile1:
    #get branch
    branchInfo = line.split(';')
    gym.addBranch(branchInfo[0],branchInfo[1],branchInfo[2].strip())
inFile1.close()

inFile2 = open('member_data.txt', 'r')

#for each line
for line in inFile2:
    #split line data
    memberInfo = line.split(',')
    #create member
    member = Member(memberInfo[0],memberInfo[1],memberInfo[2],memberInfo[3].strip())
    #add member
    gym.addMember(member)
inFile2.close()
gym.sortMembers()

print('1-Update Surname\n2-Delete Member\n3-Display Histogram\n\
4-Get Branch Info\n5-Display Gym Info \n6-Exit')
choice = int(input('Enter choice:'))

while choice != 6:
    if choice == 1:        
        memberId = int(input('Enter member id to update: '))
        surname = input('Enter new surname: ')
        gym.updateMemberSurname(memberId, surname)
        print('Operation Complete..\n')
    elif choice == 2:
        memberId = int(input('Enter member id to delete: '))
        gym.removeMember(memberId)
        print('Operation Complete..\n')
    elif choice == 3:
        ageData = gym.getMemberAges()
        clf()
        hist(ageData)
        #pyplot does not show until execution finished, if draw is not called
        pause(0.1)
    elif choice == 4:
        branch = input('Enter name of branch: ')
        info = gym.findBranchInfo(branch)
        print('City:',info[0],'Tel:',info[1])
    elif choice == 5:
        print(gym)
    else:
        print('Invalid choice')
        
    print('\n1-Update Surname\n2-Delete Member\n3-Display Histogram\n\
4-Get Branch Info\n5-Display Gym Info \n6-Exit')
    choice = int(input('Enter choice:'))



