# lab5.1.6-studentDataFunction.py
# write a function that that will read in the data for the data structure in lab5.1.4
# ref https://www.w3schools.com/python/python_dictionaries.asp
# Author: Declan Fox

students = []

def student_data():
    # function to get student's name and grades
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
    return student


get_more_students = 'y'
while get_more_students == 'y':
    students.append(student_data())
    get_more_students = input("y to continue: ")

for student in students:
    print (f'Student: {student["name"]}')
    for module in student["modules"]:
        print(f"\t {module['courseName']} \t: {module['grade']}")