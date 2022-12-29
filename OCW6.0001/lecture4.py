#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 20:03:44 2022

@author: sixym3
"""

"""
Vocabulary

Decomposition: Different devices are going to work together for you to achieve 
the an end goal Ex. If you need to project a video over a large area, you don't
need a super large projecter, instead, feed different input to a set of smaller
projecters and have them work together to achieve what you want.

Abstraction: You don't need to know everything about an object, or even know 
how it works, to use it effectively. Ex. A projector, most people know how to 
use one, but does not know how the internals work together so that it just
works.

When programming, use decompositions and have a function do one task
Achieve abstraction by using docstrings/function specifications


Any arguments for a function is called Formal parameters, which doesn't have
any value yet

Actual parameters are the values actually passed into the function when the
function is called

When a function is called, a new scope is created and variable names are not shared

"""

def is_even(i :int) -> bool:
    """
    Returns True if i is even, otherwise False.
    
    Parameters
    ----------
    i : a positive integer
        
    Returns 
    -------
    Boolean

    """
    return i % 2 == 0
    

def func_a():
    print("inside function a")
    
def func_b(y):
    print("inside function b")
    return y

def func_c(z):
    """
    

    Parameters
    ----------
    z : TYPE
        DESCRIPTION.

    Returns
    -------
    z : TYPE
        DESCRIPTION.

    """
    print("inside function c")
    print(type(z))
    return z()

x = 5

def func_d():
    print(x)
    print(x + 3)

print(func_a())
print(5 + func_b(2))
print(func_c(func_a))
func_d()





"""
for i in range(20):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")
"""