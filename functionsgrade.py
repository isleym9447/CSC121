# -*- coding: utf-8 -*-


# 1. ask user for number of students
# 2. ask user for number of tests they want to enter scores for

# 3.
# ask for first student name
# ask for first test name and score
# do the same for remaining tests

# after having entered scores for all tests, move on to next student and repeat

# 4. 
# last caluclate the average score for each student.



def get_lettgrade(score):
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade




















