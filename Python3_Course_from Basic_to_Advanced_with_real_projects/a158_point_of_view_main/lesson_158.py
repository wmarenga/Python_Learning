from lesson_158_package.module import say_hi, sum_of_module
from sys import path

import lesson_158_package.module
from lesson_158_package import module
# from lesson_158_package.module import *
# import lesson_158_package.module

# from lesson_158_package.module import sum_of_module

# print(*path, sep='\n')
print(sum_of_module(1, 2))
print(lesson_158_package.module.sum_of_module(1, 2))
print(module.sum_of_module(1, 2))
# print(variable) # wrong
print(module.variable)  # right
# print(new_variable) # wrong
print(module.new_variable)  # right
# # print(*path, sep='\n')
# print(sum_of_module(1, 2))
# print(lesson_158_package.module.sum_of_module(1, 2))
# print(module.sum_of_module(1, 2))
# print(variable)
# print(new_variable)

print(__name__)
say_hi()
