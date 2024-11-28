# print(name)
# name="sadhana"
# age=33


name="sneha"
age="10"
print(name)
print(age)
print("hello everyone muy name is " + name +"i am " + age + "years old")
name =input("enter your age")
print(name)
#       //Variables
#  name="sadhana"
#  age=33
#  print("hello worls", name,age)
#  print(name)
#  print(age)


 
#    	//fetching input
#   name= input("your name")
#   print(name)
 
#   print("Hello Tony")
#   name = input("Hello tony what is your superhero name ")
#   print( "Oh so your superhero is " +name)

#      //Type conversion can be done using int(), float(), str(), bool() fucnctions : for example

#   old_age=input("enter your old age : ")
#   new_age = int(old_age) + 3
#   print(new_age)


#     // program to fins sum of two numbers
 
#   first = input("eneter the first value")
#   second = input("eneter the second value")
#   result = int(first)+ int(second)
#   print(" the sum of two number is :" + str(result))

#       //String and methods of string  .upper(), .find(), .lower(), .replace(actual, toreplace), in

#   name= "tony kakkar"
#   print(name.replace("tony kakkar", "Sadhana Mehta"))
#   print(name)

#   print(name.find('tony'))
#   print(name.upper())

#       //Keywords in returns true or false

#   print("tony" in name)
#   print ("sadhana" in name)

#      //Arithmetic operators : addition +, multi *, division /, // gives only integer removes decimal, % modulus, **power.

# num = 10 ** 2
# print(num)

# num =19/3
# print(num)

# num =19//3
# print(num)

# num = 10
#   num = num+5      can be written as
# num += 5
# print(num)

# num-=5
# print(num)

# num *=5
# print(num)

#  //operator preceedence based on their preceedance multi, division, addition

#      //comparision operator >, <, >=, <=, !, ==, =!,
#      //Logical operator or, and ,

# print(2>3 or 3>4)
# print(2>3 and 3>3)

# name = Sadhana mehta
# print("s" in name)

# If- else statement
# python doesnot uses braces to represent block of code , python uses : 

# age=input("enter your age in number")
# result= int(age)
# if result>15 and result<19:
#     print("you are not a child ")

# elif result>19 and result<30:
#     print("you can vote")

# else:
#     print("Go to school")

#calculator
# first = input("enter your  first number :")
# second = input ("enter your second number :")
# operator= input("enter the operation to be performed (+,_,*,/,%) : ")

# first=int(first)
# second=int(second)

# if operator =="+":
#     print(first+second)
# elif operator == "-":
#     print(first-second)
# elif operator =="*":
#     print(first*second)
# elif operator =="/":
#     print(first/second)
# elif operator =="%":
#     print(first%second)
# else:
#     print("invalid operator")   

#Range keyword prints the list of numbers from 0 to the given range

# number =range(9)                            # prints 0,1,2,3,4,5,6,7,8

# print(number)                   # prints 1,2,3,4,5,6,7,8,9

# i=5
# while i>=0:
#     print(i * "*")
#     i=i-1


# i=1
# while i<=5: 
#     print(i)
#     i=i+1


# i=1
# while i<=5:
#     print(i * "*")
#     i=i+1


#for loops are used to iterate over a sequence (list, tuple, dictionary, set, string) or other iterable objects.
# for i in range(0, 10):
#  print(i+1)

#Lists collection of items - complex data type
# marks =[10,20,30,40,50]
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[-1 ])      #-1 prints the last element in the list
# print(marks[-2 ])      #-2 prints the second last element in the list

# print(marks[0:2])    #prints the elements from 0 to 2-1 ie: 10, 20

# for score in marks:
#     print(score)

# marks.append(1000)     #adds new element at the end of the list
# print(marks)

# marks.insert(0, 1000)  #adds the element at the given index here: index is 0 and eleemnt is 1000
# print(marks)
# marks.remove(1000)     #removes the element from the list
# print(marks)


# print(1000 in marks)   #checks whether the element is present in the list or not
# print(1000 not in marks)   #checks whether the element is not present in the list or not
# print(len(marks))   #prints the length of the list
# print(marks.count(10))   #prints the number of times the element is present in the list

# #loops in lists

# i=0
# while i<len(marks):
#     print(marks[i])
#     i=i+1

# marks.clear()
# print(marks)

#Break and continue statements

# students = ["Rahul", "Rohan", "Raj", "Rajesh", "Rahul"]

# for student in students:
#     if student == "Rahul":     #we are printing students except Rahul
#         break;
#     print(student)

# for student in students:
#     if student=="Rahul":     #continue statement is used to skip the current iteration ie: Rahul
#         continue;
#     print(student)


#Tuple is like list but cannot be changed once defined   ()

# marks=(10,20,30,40,50,60,70,80,90,100, 100, 100)
# marks = 10, 20, 30   # tuple can be defined without using ()
# print(marks.count(100))      #prints the occurances of the element 10 
# print(marks.index(100))      #prints the index of the element 10
# print(marks[0:5])   #prints the elements from index 0 to 5

#Sets are defined within {} and are unordered and cannot have duplicate elements elements 
#are not accessed by index value :

# marks ={10,20,30,40,50}
# for score in marks:
#     print(score)

#Dictionary is defined within {} and is unordered and cannot have duplicate elements
# stored in key value pairs

# marks ={"Hindi" :10, "english": 20, "maths": 30, "science": 40, "social": 50}
# print(marks["maths"])
# print(marks)

#Functions are defined using def keyword and can be called using the function name followed by ()
# 1 Inbuilt functions  ex: int(), float(), str(), len(), print(), input(), type()
# 2 User defined functions
# 3 module functions   ex: import math, math.sqrt(), math.pow() 
# import math
# print(dir(math))  #importing math module and printing all the functions available in the math module

# from math import sqrt   
# print(sqrt(16))    #importing only sqrt function from math module

# from math import *
# print(sqrt(16))    #importing all the functions from math module

#User defined functions
        # def function_name(parameters):
        #     function body

# def sum(a,b):
#      print(a+b)
# sum(1,2)

# def sum(a,b=2):
#     print(a+b)
#     sum(1)
# =======================================================================
# File handling in python       # open() function is used to open a file and return a file object
# OOPs in python # Inheritance in python