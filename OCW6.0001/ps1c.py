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

best_saving_rate = 5000 # from 0 to 10000

def savings_after_period(saving_rate, salary, period):
    semi_annual_raise = .07
    r = 0.04
    saving = 0
    for i in range(period):
        saving += (saving * r / 12)
        saving += (saving_rate * salary / 12)
        if i % 6 == 0:
            salary += (salary * semi_annual_raise)
    return saving

guess = 0
upper = 10000
lower = 0
print(savings_after_period(best_saving_rate/100000.0, annual_salary, number_of_months))


while abs(down_payment - guess) > epsilon:
    print(lower)
    if guess > down_payment:
        lower = best_saving_rate
    else:
        upper = best_saving_rate
    best_saving_rate = (upper + lower) / 2
    guess = savings_after_period(best_saving_rate/10000.0, annual_salary, number_of_months)

print(best_saving_rate)
