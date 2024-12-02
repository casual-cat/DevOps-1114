# print ("what's your name?")
# name = input()
# print ("what's your age?")
# age = int(input())

# print (f"your name is {name} and your age is {age}")
# currentyear = 2024
# age100 = currentyear - int(age) + 100
# print (f"you will be 100 years old in {age100}")
#-------------------------------
# print ("give a number:")
# num = int(input())
# if num % 2 == 0 and num % 4 != 0:
#     print ("even")
# elif num % 4 == 0:
#     print ("divisible by 4")
# else:
#     print ("odd")
#-------------------------------
list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = []
for number in list1:
    if number < 5:
        list2.append(number)
print (list2)