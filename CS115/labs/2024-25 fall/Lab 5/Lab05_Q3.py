#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 19:46:33 2024

"""

def add_student(students, key, value):
    if key not in students:
        students[key] = []
        students[key].append(value)
        print('Student Added')
    else:
        print('Student already exists')
        
def add_course(students, key, value):
    if key in students:
        students[key].append(value)
    else:
        print('Student not found')
        
def find_student(students, key):
    if key in students:
        return students[key]
    else:
        print('Student does not exist')
        return None
        
students = {}
choice = int(input('1)Add Student\n2)Search Student\n3)Add Course Grade\n4)Show All Students\n5)Quit\nEnter Choice:'))
while choice != 5:    

    if choice == 1:
        student_id = input('Enter student number: ')
        course = input('Enter course: ')
        grade = float(input('Enter grade: '))
        add_student(students, student_id, (course, grade))
        
    elif choice == 2:
        student_id = input('Enter student number: ')
        student = find_student(students, student_id)
        if student != None:
            print("List of courses and grades:", student)
    elif choice == 3:
        student_id = input('Enter student number: ')
        course = input('Enter course: ')
        grade = float(input('Enter grade: '))
        add_course(students, student_id, (course, grade))
    elif choice == 4:
        print('All students:', students)
    else:
        print('Invalid choice')
    
    choice = int(input('1)Add Student\n2)Search Student\n3)Add Course Grade\n4)Show All Students\n5)Quit\nEnter Choice:'))


print('Program Ended....')

