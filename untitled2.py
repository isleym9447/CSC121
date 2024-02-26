# -*- coding: utf-8 -*-





students = [["Jon", 78,75,76,"C"],["Sue",100,100,100,"A"]]


# get number of tests

tests = ["quiz1","quiz2"]




#get name of quizzes iterate over tests list


    
#header row 
print(f'{"Name":<10}', end="") 

for test in tests:
    print(f'{test:<10}',end="")
print(f'{"Avg":<10}{"Grade"}')

#iterate over list of list

for student in students:
    #iterate over inner list
    
    for i in student: 
        print(f'{i:<10}', end="")
    print()


