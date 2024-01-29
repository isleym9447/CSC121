# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Tax calculator
# 1-24-2024
# CSC121 M1Lab1– Review
# Mattea Isley


# get input from user in order to determine if program will run or not. 
# ie single will run program, stop will terminate and anything else will be invalid
status = input("Enter marital status (Single, Married, Divorced...): ")
# use first inputted data 
while status != "stop":
    
#they entered single, so program will run
    
    if status == "single":
        
# begin calculations

# ask for input, this time their income for the calculations
        income = float(input("\nEnter your income: $"))

# if they enter 0, that means no income which means no taxes, they need to try again
        if income == 0:
            print("\nYou entered $0 as your income. If this was an error, try again.")
            
            income = float(input("\nEnter your income more than $0: $"))
        #1        
        if income <= 9875:
            
            marg = .10
            inc_tax = income * marg
            eff = inc_tax/income
            
            print(f'\nMarginal Tax Rate: {marg} or 10% of your income.')
            print(f'\nIncome Tax Rate: {income * marg}')
            print(f'\nEffective Tax Rate: {inc_tax / income}')
        #2   
        elif income <= 40125:
            marg = .12
            inc_tax = 986 + (income - 9876) * marg
            eff = inc_tax/income
            
            print(f'\nMarginal Tax Rate: {marg} or 12% of your income.')
            print(f'\nIncome Tax Rate: {income * marg}')
            print(f'\nEffective Tax Rate: {inc_tax / income}')
        #3    
        elif income <= 85525:
            marg = .22
            inc_tax = 4168 + (income - 40126) * marg
            eff = inc_tax/income
            
            print(f'\nMarginal Tax Rate: {marg} or 22% of your income.')
            print(f'\nIncome Tax Rate: {income * marg}')
            print(f'\nEffective Tax Rate: {inc_tax / income}')
        #4
        elif income <= 163300:
            marg = .24
            inc_tax = 14606 + (income - 85526) * marg
            eff = inc_tax/income
            
            print(f'\nMarginal Tax Rate: {marg} or 24% of your income.')
            print(f'\nIncome Tax Rate: {income * marg}')
            print(f'\nEffective Tax Rate: {inc_tax / income}')
        #5
        elif income <= 207350:
            marg = .32
            inc_tax = 33272 + (income - 163301) * marg
            eff = inc_tax/income
            
            print(f'\nMarginal Tax Rate: {marg} or 32% of your income.')
            print(f'\nIncome Tax Rate: {income * marg}')
            print(f'\nEffective Tax Rate: {inc_tax / income}')
        #6
        elif income <= 518400:
            marg = .35
            inc_tax = 47386 + (income - 207351) * marg
            eff = inc_tax/income
            
            print(f'\nMarginal Tax Rate: {marg} or 35% of your income.')
            print(f'\nIncome Tax Rate: {income * marg}')
            print(f'\nEffective Tax Rate: {inc_tax / income}')
        #7  
        elif income >= 518401:
            marg = .37
            inc_tax = 156235 + (income - 518401) * marg
            eff = inc_tax/income
            
            print(f'\nMarginal Tax Rate: {marg} or 37% of your income.')
            print(f'\nIncome Tax Rate: {income * marg}')
            print(f'\nEffective Tax Rate: {inc_tax / income}') 
        #7 
        elif income <= 518401:
            marg = .37
            inc_tax = 156235 + (income - 518401) * marg
            eff = inc_tax/income
            
            print(f'\nMarginal Tax Rate: {marg} or 37% of your income.')
            print(f'\nIncome Tax Rate: {income * marg}')
            print(f'\nEffective Tax Rate: {inc_tax / income}')
            
        again = input("\nWould you like to run again? Type yes or no: ")
        
        if again == "yes":
            status = "single"
        elif again == "no":
            status = "stop"

# end calculations PHEW

# they entered anything other than single or stop which is invalid so it will prompt for another answer
    else:
        print("\nSorry, this calculator is for singles only!")
            
        status = input("\nPlease enter marital status (Single, Married, Divorced...) or enter 'stop' to terminate program: ")
        
            
print("\nThanks for using! Good luck on your taxes! :) ")






    
    
    

    

    
    
    

   

        
    










    


    
   