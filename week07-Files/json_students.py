# json_students.py
# adds to lab6.1.2-student_management.py
# Author: Declan Fox
import json

FILENAME = "students.json"
students= []

def display_menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(l) Load students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/s/l/q):").strip()
    return choice

def do_add(students):
    currentStudent = {}
    currentStudent["name"]=input("Enter name :")
    currentStudent["modules"]= read_modules()
    students.append(currentStudent)
    print("in adding")

def read_modules():
    modules = []
    module_name = input("\tEnter the first Module name (blank to quit) :").strip()

    while module_name != "":
        module = {}
        module["name"]= module_name
        # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        # now read the next module name
        module_name = input("\tEnter next module name (blank to quit) :").strip()
    return modules

def display_modules(modules):
    print ("\tName \tGrade")
    for module in modules:
        print(f'\t{ module["name"]} \t{ module["grade"]}')

def do_view(students):
    for currentStudent in students:
        print(currentStudent["name"])
        display_modules(currentStudent["modules"])
    print("in viewing")

def do_save(students):
    write_dict(students)
    print("students saved")
    print("in save")

def write_dict(obj):
    with open(FILENAME, 'wt') as f:
        json.dump(obj,f)

def read_dict():
    # this will throw an error if the file does not exist
    # it should readly just return an empty dict
    # we can do this later
    with open(FILENAME) as f:
        return json.load(f)

def doLoad():
    return read_dict()


#main program
choice = display_menu()
while(choice != 'q'):
    # we could do this with lamda functions
    # I am keeping this basic for the moment
    if choice == 'a':
        do_add(students)
    elif choice == 'v':
        do_view(students)
    elif choice == 's':
        do_save(students)
    elif choice == 'l':
        students = doLoad()
    elif choice !='q':
        print("\n\nPlease select either a,v,s,l or q")
    choice=display_menu()
