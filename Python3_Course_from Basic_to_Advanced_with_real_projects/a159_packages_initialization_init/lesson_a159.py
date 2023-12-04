# from sys import path
# https://stackoverflow.com/questions/2386714/why-is-import-bad

# import lesson_a159_package.module
# from lesson_a159_package import module


# print(module.sum_of_module(1, 2))
# print(variable)
# print(new_variable)
from lesson_a159_package import say_hi, sum_of_module


print(__name__)
say_hi()
# print(__name__)
# say_hi()


print(sum_of_module(2, 3, 6))
say_hi()
