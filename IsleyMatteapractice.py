# -*- coding: utf-8 -*-



#ask user for their income
income = float(input("Enter your yearly income: "))


# check

if income >= 40_000:
    
    #ask for years worked
    
    years = float(input("Enters the number of years worked: "))
    
    if years >= 2:
        
        print("Congrats! You are approved for the loan!")
    else:
        
        print("Sorry! You havent worked for 2 or more years!")
else:
    print("Sorry! You havent worked for 2 or more years!")




