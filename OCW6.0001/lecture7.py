#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 10:41:39 2023

@author: sixym3
"""

"""
Make the program more modular so it is easier to test module by module
Unit testing - validate each piece of program and test each function seperately
Regression testing - add test for bugs as you find them, and catch reintroduced 
error that was previously fixed
Integration testing - test the overall program

Black box testing - creating test cases on specifications only, use extreme 
values, boundry cases, empty lists, singleton lists

glass box testing - use code to guide the design of test cases
path complete if every potential path through the code is tested at least once
Branches - execute all parts of a conditional
For loops - loop not entered, loop entered once, loop entered more than once
While loops - Same as to loops, plus all the ways to exit loop (break)

Raise exceptions and stop the running of the program is better than returning
an error value

raise ExceptionName (Descriptions)

AssertionError
"""

assert True, "not true"