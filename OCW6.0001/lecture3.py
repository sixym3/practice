#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 22:11:05 2022

@author: sixym3
"""
import math

def cheerleader():
    text = input("I will cheer for you, give me a word:  ")
    num = int(input("How enthuastic are you [1-10]"))
    
    for char in text:
        print("Give me an", char, ":", char)
        
    print("What does that spell?!")
    
    for i in range(num):
        print(text)
        
def cuberootgac(x = 8):
    guess = 0
    for guess in range(abs(x)+1):
        if guess ** 3 >= abs(x):
            break
    if guess ** 3 != abs(x):
        print(x, "is not a perfect cube", guess)
    else:
        if x < 0:
            guess = -guess
        print("The cube root of", x, "is", guess)
        
def cuberootapp(x = 8):
    epsilon = 0.001
    guess = 0
    increment = 0.0001
    while abs((guess ** 3) - x) >= epsilon and guess ** 3 <= x:
        guess += increment
    if abs((guess ** 3) - x) > epsilon:
        print("Failed to find cube root of", x, "with final guess as", guess)
    else: 
        print("Found the cube root of", x, "to be", guess,"Calculated with **:", x ** (1. / 3))
    

def cuberootbisection(x = 8):
    """
    Give an search space of N, if 
    1 -> N/(2^1)
    2 -> N/(2^2)
    ...
    k -> N/(2^k)
    Assume the k-th search finds the answer, and there is only one answer, 1 = N/(2^k) such that
    2^k = N -> k (number of searches) -> (is dependent on) log_2(N)
    complexity: log_2(N) which is also log(N)
    """
    minimum = 0
    maximum = x
    guess = ( minimum + maximum ) / 2
    epsilon = 0.001
    while abs(guess ** 3 - x) > epsilon:
        if guess ** 3 > x:
            maximum = guess
        else:
            minimum = guess
        guess = ( minimum + maximum ) / 2
    print("cube root of", x, "is", guess, x ** (1./3))
    
        
if __name__ == "__main__":
   cuberootbisection(10000)
   
   
