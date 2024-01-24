# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



# ask user to enter start, end and step value


start = int(input("Enter starting number: "))

end = int(input("Enter ending number: "))

step = int(input("Enter step value: "))

#define header row
# < left alined 7
# "-"*18 for 18 -

print(f'\n{"Num":<7}{"Sqr":<7}{"Cube"}')
print("-"*18)

#start the loop

#for acending order, step is positiive and +1 to the end value
#for decending order, step is negative and -1 to the end value



for num in range(start, end-1, step):

    sqr = num **2
    print(f'{num:<7}{sqr:<7}{num**3}')






