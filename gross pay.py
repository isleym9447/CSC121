# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 13:32:32 2024

@author: isleym9447
"""



#define and assign initial value before the loop begins
#running total to cal total of salaries owed

total = 0 #store salaries
#count = 0 #to count employees

# calculate gross pay

name = input("Enter employee name or 'stop' to terminate program: ")


while name != "stop":

    print("\nInfo for", name)
    hours = float(input("Enter hours worked: "))
    while hours < 0 :
        
        print("\nINVALID ENTRY!")
        print("Must be between 0 and 40")
        hours = float(input("\nEnter hours worked again: "))
    
    
    
    rate = float(input("Enter pay rate: "))
    
    gross = hours * rate
    
    # total = total + gross
    
    total += gross
    
    
    #another option:        print("Gross pay $", gross, sep='')
    
    print(f'Gross pay: ${gross}')
    
    name = input("Enter next employee name or 'stop' to terminate program: ")

    print(f'\nTotal Salaries: ${total}')
    











