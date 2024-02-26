# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 13:24:36 2024

@author: isleym9447
"""
import functionsgrade as fn


def main():
    
    #ask for names
    test_num = int(input("Enter number of tests: "))
    #create a list with test names
    tests = []
    
    
    for x in range(test_num):
        
        test_name = input("Enter test name: ")
        
        tests.append(test_name)
    
    
    #ask for number of students
    stu_num = int(input("Enter number of students: "))
    
    
    students = []
    for x in range(stu_num):
        student = []
        stu_name = input("Enter student name: ")
        student.append(stu_name)
        
    #enter score for each test
        for test in tests:
            
            print("Enter score for", test)
            
            score = float(input())
            
            student.append(score)
            
        scores = student[1:] 
        
        #get average
        
        avg = sum(scores) / len(scores)
        #append to student list
        student.append(avg)
        
        # get letter grade
        grade = fn.get_lettgrade(avg)
        
        
        
        student.append(grade)
        students.append(student)
            
        #print(f'{name}{test_name}{score}{avg}{grade}')
        
        
        
        
        
        
    # student1 [name, scores, _, _, _]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    
    main()