#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 20:20:46 2023

@author: sixym3
"""

annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ​"))
total_cost = float(input("Enter the cost of your dream home:​ "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
r = 0.04
current_savings = 0.0
portion_down_payment = 0.25
number_of_months = 0

while total_cost * portion_down_payment > current_savings:
    current_savings = current_savings + (current_savings * (r / 12))
    current_savings += (annual_salary / 12 * portion_saved)
    number_of_months += 1
    if number_of_months % 6 == 0:
        annual_salary += (annual_salary * semi_annual_raise)

print("Number of months:​ ", number_of_months)