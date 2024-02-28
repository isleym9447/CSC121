# -*- coding: utf-8 -*-


# dictionaries

import functions as fn
def main():

    test_nums =int(input("Enter number of tests: "))
    
    
    
    
    # create a list with test names
    tests = []
    
    for x in range(test_nums):
        
        test_name = input("Enter test name: ")
        
        tests.append(test_name)
    
    #ask for number of students
    stu_nums = int(input("Enter num of students: "))
    
    #create a list to hold all student dictionaries
    
    students = []
    for x in range(stu_nums):
        stu = {} #empty dictionary for each student
        # ask for name and add to dict
        stu_name = input("Enter student name: ")
        
       # stu.update({"Name":stu_name}) 
        
        stu["Name"]= stu_name

    #get score for each tent and add to dictionary
    
    #define accumulator variable before loop
    
    scores = 0
    for test in tests:
        
        score = float(input("Enter score for"+test+": "))
        
        scores += score
        
        #add to dict
        
        stu[test] = score
        
    #get avg
    
    avg = scores/test_nums
    
    #add to dict
    
    stu["avg"]= avg
    
    #add letter grade
    
    stu["grade"] = fn.get_letgrade(avg)
    
    #append it to list of students
    
    students.append(stu)
    
    
    


if __name__ =="__main__":
    
    main()