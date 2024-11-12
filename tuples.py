#        1
# my_tuple = (1, 2, 3)
# print(my_tuple)
# print(my_tuple[1])
# my_tuple[0] = 10
# print(my_tuple)

#                2
# person_tuple= ("gabi", 20, "ohio")
# name, age, city = person_tuple 
# print(age)
# print(name)
# print(city)

#                  3
# nested_tuple = ((1, 2, 3), (4, 5, 6))
# print(nested_tuple[0][2])

#                4
# tuple_numbers = (1, 2, 3, 2, 4, 2)
# count= tuple_numbers.count(2)
# print(count)
# find= tuple_numbers.index(3)
# print(find)

#                                      ---DICTIONARIES---
#               1
# student = {
#     "name": "gabi",
#     "Age": 20,
#     "Grade": "wtf"
# }
# print(student["name"])
# student["school"] = "sela"
# print(student)
# student["Age"] = 21
# print(student)
# student.pop("Grade")
# print(student)

#            3
# capitals = {
#     "france": "paris",
#     "spain": "madrid",
#     "japan": "tokyo"
# }
# for country in capitals:
#     print(f"the capital of {country}, is {capitals[country]}")
# print(capitals.values())
# print(capitals.keys())
# print(capitals.items())
# japan1 = capitals.get("japan")
# print(japan1)
# capitals.setdefault("germany", "not found")
# # germany = capitals.get("germany")
# print(capitals.get ("germany"))


#- Write a program that counts the number of times each character appears in a given string. For example text = 'hello'
#Expected output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def count_words(text):
  count = {}
  for i in text:
      if i in count:
          count[i] += 1
      else:
          count[i] = 1
          return count 
      text = "hello"
      result = count_words(text)
      print(result)
      
      
#                      ----SETS----
# my_set= {1, 2, 3, 4, 5}
# my_set.add(6)
# print(my_set)
# # my_set.add(3)
# # print(my_set)
# my_set.remove(2)
# print(my_set)

#       2
# set_a= {1, 2, 3, 4}
# set_b= {3, 4, 5, 6}
# union= set_a.union(set_b)
# print(union)
# intersection= set_a.intersection(set_b)
# print(intersection)
# diff= set_a.difference(set_b)
# print(diff)
# sym= set_a.symmetric_difference(set_b)
# print(sym)

#             3
# num= [1, 2, 2, 3, 4, 4, 5]
# unique= list(set(num))
# print(unique)

# set_a= {1, 2, 3, 4}
# if 6 in set_a:
#     print(True)
# else:
#     print(False)

set_b= {3, 4, 5, 6}
# if 2 in set_b:
#     print(True)
# else:
#     print(False)
set_b.add(7)
print(set_b)
set_b.remove(7)
print(set_b)
