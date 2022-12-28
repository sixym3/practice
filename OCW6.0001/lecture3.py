#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 22:11:05 2022

@author: sixym3
"""

def cheerleader():
    text = input("I will cheer for you, give me a word:  ")
    num = int(input("How enthuastic are you [1-10]"))
    
    for char in text:
        print("Give me an", char, ":", char)
        
    print("What does that spell?!")
    
    for i in range(num):
        print(text)
        
def cuberootgac(x = 8):
    minimum = 0
    maximum = x
    guess = minimum
    for guess in range(abs(x)+1):
        if guess ** 3 >= abs(x):
            break
    if guess ** 3 != abs(x):
        print(x, "is not a perfect cube", guess)
    else:
        if x < 0:
            guess = -guess
        print("The cube root of", x, "is", guess)
        
        
if __name__ == "__main__":
   cuberootgac(-64)