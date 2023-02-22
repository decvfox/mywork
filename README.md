 ![](https://github.com/decvfox/mywork/blob/main/banner.png)

# Programmimg & Scripting Labs
This repository contains labwork from my HDip in Data Analysis

### Week 01

Most of this week's work involved setting up our machines for the course.
we set-up Cmder, Anaconda, CodeVS, Github and notepad++. 

### Week 02

#### Lab 2.1

>Do this lab in the python console.
You can start the python console by typing python on the command line this will
give a prompt that looks like 3 greater than signs >>>

#### Lab 2.2

Our first programmes. we covered the print function, inputs and string manulation.

Key takeaway/learning: f-strings string formatting 
[Click here to learn more](https://realpython.com/python-f-strings/#:~:text=Also%20called%20%E2%80%9Cformatted%20string%20literals,the%20__format__%20protocol.)

Here is an example

```python
print(f'Hello {name},\tyour age is {age}.')
```

### Week 05

#### Lab 05-Data Structures

lab5.1.2-summerMonths.py

Tuples

stores the 12 months of the year and prints the summer months

lab5.1.3-popFromList.py

Lists

A program that puts 10 random numbers into a queue(list), the
program should then output all the values in the queue, then take the
numbers from the queue one at a time, print it and the current numbers still
in the queue

```python
print ("current Number is {currentNumber} and the queue is {queue} ")
```
should be:
```python
print (f"current Number is {currentNumber} and the queue is {queue} ")
```

lab5.1.4-studentCourseGrade.py

Dicts

Write a program that stores a student name and a list of her courses and
grades in a dict, the program should then print out her data

```python
print("\t {} \t: {}".format(module["courseName"], module["grade"]))
```
updated to
```python
print(f"\t {module['courseName']} \t: {module['grade']}")
```
