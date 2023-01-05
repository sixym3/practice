#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 20:42:17 2023

@author: sixym3
"""

annual_salary = float(input("Enter your starting annual salary: "))
total_cost = 1000000
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
epsilon = 100

number_of_months = 36
semi_annual_raise = .07
r = 0.04

best_saving_rate = 5000 # from 0 to 10000

def savings_given_rate(saving_rate, salary):
    saving = 0
    for i in range(number_of_months):
        # print("function:", i, saving)
        saving = saving * (1 + (r / 12))
        saving = saving + (saving_rate * (salary / 12))
        if i % 6 == 0:
            salary = salary * (1 + semi_annual_raise)
            
    return saving

lower = 0
upper = 10000

def find_best_saving_rate(salary, lower, upper):
    global counter
    counter += 1
    best_saving_rate = round((lower + upper) / 2.0)
    # print("rate:", best_saving_rate)
    result = savings_given_rate(best_saving_rate/10000.0, salary)
    if abs(result - down_payment) > epsilon:
        if result >= down_payment:
            # return "greater"
            return find_best_saving_rate(salary, lower, best_saving_rate)
        else:
            # return "less"
            return find_best_saving_rate(salary, best_saving_rate, upper)
    else:
        return best_saving_rate
    
counter = 0
try:
    result = (find_best_saving_rate(annual_salary, lower, upper)/10000.0)
    print("Best saving rate:", result)
    print("Steps in bisection search", counter)
except RecursionError:
    print("It is not possible to pay the down payment in three years")