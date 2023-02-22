# lab5.1.4-studentCourseGrade.py
# Write a program that stores a student name 
# and a list of her courses and grades in a dict, 
# the program should then print out her data.
#Author: Declan Fox

student = {
    "name":"Mary",
    "modules": [
        {
            "courseName":"Programming",
            "grade": 45
        },
        {
            "courseName":"History",
            "grade":99
        }
    ]
}
print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print(f"\t {module['courseName']} \t: {module['grade']}")