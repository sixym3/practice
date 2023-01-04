#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 20:09:42 2023

@author: sixym3
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("TEnter the percent of your salary to save, as a decimal:​ "))
total_cost = float(input("Enter the cost of your dream home:​ "))
r = 0.04
current_savings = 0.0
portion_down_payment = 0.25
number_of_months = 0

while total_cost * portion_down_payment > current_savings:
    current_savings = current_savings + (current_savings * (r / 12))
    current_savings += (annual_salary / 12 * portion_saved)
    number_of_months += 1

print("Number of months:​ ", number_of_months)