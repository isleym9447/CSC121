# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 13:32:32 2024

@author: isleym9447
"""



#get number of employees user is calculating for 
emp_num = int(input("Enter number of employees: "))


#define and assign initial value before the loop begins
#running total to cal total of salaries owed

total = 0 

for num in range(1,emp_num+1):

# calculate gross pay
    print("\nInfo for Employee #", num)
    hours = float(input("Enter hours worked: "))
    
    rate = float(input("Enter pay rate: "))
    
    gross = hours * rate
    
    # total = total + gross
    
    total += gross
    
    
    #another option:        print("Gross pay $", gross, sep='')
    
    print(f'Gross pay: ${gross}')
    
print(f'\nTotal Salaraies: ${total}')













