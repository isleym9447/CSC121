# -*- coding: utf-8 -*-









numbers = [5,6,7,8,9,10,11,12,13,14,15]



print(f'{"Num":<5}{"Sqr":<5}{"Cube"}')
print("-"*15)

#initiate running totals

total_sqr = 0
total_cube = 0


for num in numbers: 
    
    sqr = num ** 2
    cube = num ** 3
    
    total_sqr = total_sqr + sqr
    
    total_cube += cube

    print(f'{num:<5}{sqr:<5}{cube}')
print("-"*15)   
print(f'{""*5:<5}{total_sqr:<5}{total_cube}')












