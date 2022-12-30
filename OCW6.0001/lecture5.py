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

print(quo, rem) 