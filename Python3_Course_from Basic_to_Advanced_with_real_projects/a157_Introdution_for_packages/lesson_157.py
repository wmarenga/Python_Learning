from sys import path

import lesson_157_package.module
from lesson_157_package import module
# from lesson_157_package.module import *  # bad practice
# import lesson_157_package.module as sm (new module name)

# from lesson_157_package.module import sum_of_module

# print(__name__)  # __main___
# print(*path, sep='\n')  # unpacking list (*)
# print(sum_of_module(1, 2))  # wrong
print(lesson_157_package.module.sum_of_module(1, 2))  # right
print(module.sum_of_module(1, 2))  # right
# print(variable)  # wrong
print(module.variable)  # right
# print(new_variable)  # wrong
print(module.new_variable)  # right
# print(sm.sum_of_module(2, 3))
