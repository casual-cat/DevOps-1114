# age = int(input ("what's ur age?: "))
# if age >= 18:
#     print("ur old enough")
# elif 16 <= age < 18:
#     print("almost there!")
# else:
#     print("ur a minor")

#- Write a program that checks if a number entered by the user is even or odd and prints the result.
# number = int(input("give number: "))
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")
    

 # - Given a score as an integer between 0 and 100, use if-elif-else statements to print the grade:
# grade= int(input("ur score: "))
# if 90 <= grade <= 100:
#     print("A")
# elif 80 <= grade <= 89:
#     print("B")
# elif 70 <= grade <= 79:
#     print("C")   
# elif 60 <= grade <= 69:
#     print("D")

# number= int(input("give number: "))
# if number > 0:
#     print("positive")
# elif number < 0:
#     print("negative")
# elif number == 0:
#     print("zero") 
    
# age= int(input("what ur age?: "))
# student= input("are u a student?: ")
# if age <= 18 or student == "yes":
#     print("u have a discount")
# else:
#     print("u pay full.")

# for number in range(1, 11):
#     if number % 2 == 0:
#         print(number)
    
# total_sum = 0
# for number in range(1, 101):
#     total_sum += number
# print(total_sum) 

#- Write a program that prints the multiplication table for a number entered by the user.

# number= int(input("give number: "))
# number2= int(input("give number: "))
# sum= int(number * number2)
# print(sum)

# list = ["red", "blue", "green"]
# for color in list:
#     print(color)

# import random
# number = random.randint(1, 11)
# while True:
#     guess = int(input("give number: "))
#     if guess == number:
#         print("correct")
#         break
#     elif guess < number:
#         print("too low")
#     else:
#         print("too high")

# total_user = 0
# while True: 
#     number = int(input("give number: "))
#     if number < 0:
#         break
#     else: 
#         total_user += number 
#         print("the total is: ", total_user)
# print("the final total is: ", total_user)

#                               ----FUNCTIONS---
# def greet(name):
#     print("hello, "+name+"!")
# greet("world")

# def greet(name):
#     name = input("what ur name?: ")
#     print("hello, "+name+"!")
# greet("world")
# if greet.isdigit():
#     print("please write your name!")

# def square(number):
#     return number * number
# print(square(4)) 

# def celsuis_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit 
    