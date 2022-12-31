#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 09:00:48 2022

@author: sixym3
"""

"""
Recursion - divde/decrease and conquer
reducing a problem to a simplier version of the same problem
A function calls it self again and again
A base case to prevent infinite recursions 

Iterative algorithems, Ex. for loops, while loops, and can be captured by 
state variables: values that tell us excatly which stage the algorithm is in

Disctionaries - also mutable

Mathmatical Induction
To prove a statement which is indexed on integer is true for all values of n:
    1) Prove that it is true when n is it's smallest value
    2) Prove that it is true for an arbitary value n, one can show it must be
    true for n+1
    
Induction example:
    0 + 1 + 2 + ... + n = ((n)(n+1))/2
    
1) Prove for smallest value of n = 0
    0 = ((0)(0+1))/2 = 0 True
2) Suppose some value of k is true for this statement, prove that k+1 also is
    true
    1 + 2 + ... + k = ((k)(k + 1))/2
    1 + 2 + ... + k + (k + 1) = ((k + 1)(k + 2))/2
    ((k)(k + 1))/2 + (k + 1) = ((k + 1)(k + 2))/2
    k^2 + 3k + 2 = k^2 + 3k + 2 True
    
Therefore, this expressions is true for all values of n > 0
"""

def multi_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

def multi(a, b):
    """
    Not solving for edge cases such as b = 0 or a negative value
    """
    if b == 1:
        return a
    else:
        return a + multi(a, b-1)
    
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def factorial_iter(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

print(factorial_iter(3))