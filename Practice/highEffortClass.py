# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 11:10:48 2023.

@author: doga
"""

class fren(object):
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
    def getName(self):
        n = self.__name
        return n
    def getAge(self):
        a = self.__age
        return a
    def getGender(self):  # genders are converted to a user-friendly version
        g = self.__gender
        if g.lower() == 'f':
            return 'female'
        elif g.lower() == 'm':
            return 'male'
        elif g.lower() == 'n':
            return 'non-binary'
        elif g.lower() == 'o':
            return 'other'
    def setAge(self, a):
        self.__age = a
    def setGender(self, a):
        self.__gender = a
    def __eq__(self, o):  # not sure what i'm doing here but it works
        return str(self.__name) == o
    def __repr__(self):
        return f'[{self.__name}, {self.__age} year-old {fren.getGender(self)}]'
    def __str__(self): # whenever i try to split the below line into two, it
    # only returns something partially. here is what i tried:
    # return f'The friend {self.__name} is {str(self.__age)} years old and '
    # 'their gender is "{fren.getGender(self)}".'
    # i thought it would look better visually. however, a non-functional but
    # visually appealing code is of no use.
        return f'The friend {self.__name} is {str(self.__age)} years old and their gender is "{fren.getGender(self)}".'
def frenChecker(t,n):
    global frenCheckerTuple
    if n not in t:
        t.append(n.lower())
        return True
    else:
        return False
def otherAdder(n, k):
    global frenList
    frenAge = input('Enter the age of your friend: ')
    while frenAge.isdigit() is not True:
        print('That is not an integer.')
        frenAge = input('Please enter a valid number: ')
    frenGender = input('Enter the gender of your friend ("f" for female, "m"'
                       ' for male, "n" for non-binary, "o" for other): ')
    while frenGender.lower() not in ['n', 'm', 'f', 'o']:
        print('That is not a valid letter.')
        frenGender = input('Please enter a valid letter for gender: ')
    k.append(fren(n, frenAge, frenGender))
    print('Friend added to the list!')
def actionPerformer(e):  # reduced lines from 360 to 198 (excluding comments)
    global frenList
    global frenCheckerTuple
    print('Here are the actions you can perform: ')
    print('1) Change the age of friend')
    print('2) Change the gender of friend')
    print('3) Remove friend')
    print('4) Exit')
    selec = input('Pick a number: ')
    if selec.isdigit() and selec in ['1', '2', '3', '4']:
        if selec == '1':
            newAge = input('Enter new age: ')
            if newAge.isdigit():
                newAge = int(newAge)
                randCount = -1
                for i in frenList:
                    randCount += 1
                    if i.getName().lower() == e.lower():
                        frenList[randCount].setAge(newAge)
                        print(f'Age changed to {newAge}!')
                        break
            else:
                while newAge.isdigit() is False:
                    print('Thats no a valid age.')
                    newAge = input('Enter new age: ')
                randCount = -1
                for i in frenList:
                    randCount += 1
                    if i.getName().lower() == e.lower():
                        frenList[randCount].setAge(newAge)
                        print(f'Age changed to {newAge}!')
                        break
        elif selec == '2':
            newGender = input('Enter new gender (f, m, n or o)'
                              ': ')
            if newGender.lower() in ['n', 'm', 'f', 'o']:
                randCount = -1
                for i in frenList:
                    randCount += 1
                    if i.getName().lower() == e.lower():
                        frenList[randCount].setGender(newGender)
                        print('Gender changed!')
            else:
                while newGender not in ['n', 'm', 'f', 'o']:
                    print('Thats not a gender.')
                    newGender = input('Enter new gender: ')
                    newGender.lower()
                randCount = -1
                for i in frenList:
                    randCount += 1
                    if i.getName().lower() == e.lower():
                        frenList[randCount].setGender(newGender)
                        print('Gender changed!')
        elif selec == '3':
            frenCheckerTuple.remove(e)
            if e.isalpha():
                randCount = -1
                for i in frenList:
                    randCount += 1
                    if i.getName().lower() == e.lower():
                        frenList.remove(frenList[randCount])
                        # 124 took me longer than I expected. it was hard to
                        # come up with this idea.
                        break
            print('Friend removed!')
        else:
            print('See you next time then!')


frenList = []
frenCheckerTuple = []  # used to be a tuple. not anymore bc it got too dificult
frenName = input('Enter the name of your friend: ')
while frenName.isalpha() is not True:
    print('That is not a string.')
    frenName = input('Please enter a valid name: ')
if frenChecker(frenCheckerTuple, frenName):
    otherAdder(frenName, frenList)
    k = input('Would you like to add another friend? (yes/no): ').lower()
    k.strip()
    if k == 'yes':
        while k != 'no':
            frenName = input('Enter the name of your friend: ')
            while frenName.isalpha() is not True:
                print('That is not a string.')
                frenName = input('Please enter a valid name: ')
            if frenChecker(frenCheckerTuple, frenName):
                otherAdder(frenName, frenList)
            else:
                while not frenChecker(frenCheckerTuple, frenName):
                    print('A friend with that name exists already.')
                    frenName = input('Please enter another one: ')
                otherAdder(frenName, frenList)
            k = input('Would you like to add another friend? (yes/no): ')
            k.lower().strip()
        o = input('Okay, would you like to see a list of your friends?'
                  ' (yes/no) :')
        if o.lower() == 'yes':
            print('Here is the list:\n', frenList)
        else:
            u = input('Well, would you like to modify a friend?'
                      ' (yes/no) :')
            if u.lower() == 'no':
                print('Alright, bye!')
            else:
                e = input('Who would you like to modify?: ')
                if e.lower() not in frenCheckerTuple:
                    while e.lower() not in frenCheckerTuple:
                        print('That name does not exist.')
                        e2 = input('Would you like to enter another name?'
                                   ' (yes/no): ')
                        if e2.lower() == 'yes':
                            e = input('Who would you like to modify?: ')
                        else:
                            print('Until next time then!')
                            break
                    actionPerformer(e)
                else:
                    actionPerformer(e)
    else:
        o = input('Okay, would you like to see a list of your friends?'
                  ' (yes/no) :')
        if o.lower() == 'yes':
            print('Here is the list:\n', frenList)
        else:
            u = input('Well, would you like to modify a friend?'
                      ' (yes/no) :')
            if u.lower() == 'no':
                print('Alright, bye!')
            else:
                e = input('Who would you like to modify?: ')
                if e.lower() not in frenCheckerTuple:
                    while e.lower() not in frenCheckerTuple:
                        print('That name does not exist.')
                        e2 = input('Would you like to enter another name?'
                                   ' (yes/no): ')
                        if e2.lower() == 'yes':
                            e = input('Who would you like to modify?: ')
                        else:
                            print('Until next time then!')
                            break
                    actionPerformer(e)
                else:
                    actionPerformer(e)
