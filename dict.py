# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 14:24:10 2024

@author: isleym9447
"""


students = [{"name": "Jon","math":78,"sci":75,"avg":76,"grade":"C"},\
             {"name":"Sue","math":100,"sci":100,"avg":100,"grade":"A"}]

#get keys for first dictionary
    
             
for k in students[0].keys():
    print(f'{k:<10}',end="")
print()

#display content, values

for student in students:
    
    for value in student.values(): #nested dictionary
    
        print(f'{value:<10}',end="")
    print()
    




         
# # get number of tests
# tests = ["quiz1","quiz2"]

# # get name of quizzes iterate over tests list


# # header row
# print(f'{"Name":<10}',end="")
# for test in tests:
#     print(f'{test:<10}',end="")
# print(f'{"Avg":<10}{"Grade"}')

# #iterate over list of list

# for student in students:
#     # iterate over inner list
    
#     for i in student:
#         print(f'{i:<10}', end="")
#     print()