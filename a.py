# import random
# myList = [1, 'a', 4.5555, False]
# myInt = list(range(0, 9))
# colors = ['red', 'yellow', 'blue', 'green', 'grey', 'red']
# nums = [1, 3, 4, 6, 5, 5, 6, 7, 1, 2]
# colors.append("violet")

# # i = 0
# # while i < len(colors):
# #     print(colors[i])
# #     i += 1
# names = ["Le", "Adam", "Hannah"]
# output = ", ".join(names)
# print(output)

# from random import random

# def flip_coin():
#     r = random()  # from 0.00 to 0.99
#     if r > 0.5:
#         return "Heads"
#     else:
#         return "Tails"

# print(flip_coin())

# nums = [0, 1, 2, 3, 4, 5, 6, 7]
# names = ['hoang', 'hien', 'long', 'khoa', 'ly']
# even = filter(lambda x: x % 2 == 0, nums)
# friend = map(lambda x: f"my friend is {x}",
#              filter(lambda x: len(x) < 5, names))
# print(list(friend))

# for i in even:
#     print(i)

# import pdb
# pdb.set_trace()


# nums1 = [1, 5, 3]
# nums2 = [4, 2, 6]
# names = ["Thomas", "Leo", "Jack"]

# avg_grade = dict(
#     zip(
#         names,
#         map(
#             lambda pair: (pair[0] + pair[1]) / 2,
#             zip(nums1, nums2)
#         )
#     )
# )

# print(avg_grade)

# def interleave(string1, string2):
#     res = ""
#     []

# print(interleave('aaa', 'zzz'))
# from random import randint
# print(random.choice(["apple", "banana", "cheery", "durian"]))
# print(random.shuffle(["apple", "banana", "cherry", "durian"]))
# print(randint(1, 100))

# import module1
# from random import *


# print(choice([1, 2, 3]))
# module1.another_fn()

# from termcolor2 import colored

# print(colored("hello", "red"))
# help(termcolor2)


import pyfiglet
from termcolor2 import colored
available_colors = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
                    "light_grey", "dark_grey", "light_red", "light_green", "light_yellow", "light_blue"]
msg = input("What would you like to print: ")
user_color = input("What color: ")
if user_color not in available_colors:
    user_color = "yellow"
print(colored(pyfiglet.figlet_format(msg), user_color))
