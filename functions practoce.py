# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:15:06 2024

@author: isleym9447
"""

def main():
    hours_worked = float(input("How many hours have you worked this week?: "))
    pay_rate = float(input("Enter your pay rate: "))
    get_gross(hours_worked, pay_rate)
    
    
    
def get_gross(hours, pay):
    gross = hours * pay
    print("Gross:", gross)
    return gross
    
main() 

















