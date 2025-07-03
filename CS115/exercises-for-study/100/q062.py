# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 19:07:18 2024.

q: Write a program to read an ASCII string and to convert it to a unicode
string encoded by utf-8.

@author: doga
"""

# probably the hardest one i've done so far. the original
# solution is useless too..

def au(s):
    e = "".join(f"\\u{ord(i):04x}" for i in s)
    return e
a = input("say somethin': ")
u = au(a)
print(u)
