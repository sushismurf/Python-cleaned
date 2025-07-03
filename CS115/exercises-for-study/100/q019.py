# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:52:59 2024.

q: You are required to write a program to sort the (name, age, height) tuples
by ascending order where name is string, age and height are numbers.
The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'),
('Json', '21', '85'), ('Tom', '19', '80')]

@author: doga
"""

# there seems to be a small mistake in the question. there is no 'score'
# value initially, intead there is 'height'. but the input takes 'height'?
# i am going to scrap height completely and use score instead.
# also, i'm not happy with how this one turned out. there must be a
# simpler way..

def listSorter(a):
    c = []
    for i in a:
        b = i.split(',')
        if len(b) == 3:
            name = b[0].strip()
            age = int(b[1].strip())
            score = int(b[2].strip())
            c.append((name, age, score))
        cc = sorted(c, key=lambda j: (j[0], j[1], j[2]))
        out = [(name, str(age), str(score)) for (name, age, score) in cc]
    return out
def main():
    c = []
    while True:
        a = input("give comma-separated name, age, and score "
                  "(ex: joe,17,99). type 'q' to quit: ")
        if a.lower() != "q":
            b = a.split(',')
            for i in range(len(b)):
                b[i] = b[i].strip()
            if len(b) == 3:
                c.append(a)
            else:
                print("invalid input.")
        else:
            cc = listSorter(c)
            print(cc)
            break
main()
