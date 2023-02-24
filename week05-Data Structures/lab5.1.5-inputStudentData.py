# lab5.1.5-inputStudentData.py
# Write a program that will read in the data for the data structure in lab5.1.4
# ref https://www.w3schools.com/python/python_dictionaries.asp
# Author: Declan Fox

modules = []
course = ' '
grade = ' '
student_name = input("please enter a student name: ")

while course != '' or grade != '':
    course = input('Enter the course name, blank to quit: ')
    grade = input('Enter a grade, blank to quit: ')
    modules.append({"courseName": course, "grade": grade})

student = {"name": student_name,
            "modules": modules}


print (f'Student: {student["name"]}')
for module in student["modules"]:
    print(f"\t {module['courseName']} \t: {module['grade']}")
