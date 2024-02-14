# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



def main():
    
    # enter speed and number of values in hour list
    
    
    speed = float(input("Enter speed: "))
    
    h_list_values = int(input("Enter number of values in hour list: "))
    
    hours = gen_hourList(h_list_values)
    
    total = 0
    
    print(f'{"Index":<6}{"Hour":<6}{"Distance Traveled":^}')
    print("-----------------------")
    for index, hour in enumerate(hours): 
        dis = hour * speed
        
        total += dis
        print(f'{index:<6}{hour:<6}{dis:^}')
    print("-----------------------")
    
    print('\nTotal:',total)
    
def gen_hourList(n):
    
    hour_list = []
    
    
    for x in range(n):
    
        hour = int(input("Enter hour: "))
        
        hour_list.append(hour)
    
    return hour_list




if __name__ == "__main__":
    main()
