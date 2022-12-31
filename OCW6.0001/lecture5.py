#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 22:20:25 2022

@author: sixym3
"""

x = 5
y = 3

(y, x) = (x, y)

def quo_rem(x, y):
    quo = x // y
    rem = x % y
    return (quo, rem)

(quo, rem) = quo_rem(10, 3)

# (quo, rem) = (rem, quo)


def remove_dups_bad(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
            
def remove_dups(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
            
L1 = [1, 2, 3, 5]
L2 = [1, 2, 3, 5]
remove_dups(L1, L2)
print(L1, L2)

"""
Aliasing - multiple variable pointing to the same object
Cloning - duplicating an object so that there is a different copy
Mutability side effects: when there are aliases pointing to the same object
it can cause unwanted side effects if you change the object as you are changing
it for both aliases 
"""