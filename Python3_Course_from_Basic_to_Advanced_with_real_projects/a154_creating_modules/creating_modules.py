"""
Documentation:
https://docs.python.org/3/tutorial/modules.html

Modularization - Understanding your own Python modules:
- The first module executed is called __main__;
- You can import another entire module or part of the module;
- Python knows the folder where __main__ is and the folders below it.
It does not recognize folders and modules above __main__ by default;
- Python knows all modules and paths packages present in the sys.path.

"""
# ! Example 1:
import calculations
import sys

# ? We will include another way for Python to search for modules.
# sys.path.append("C:/folder_name")

print(*sys.path, sep='\n')
print('This module is called: ', __name__)

# ! Example 2:
# # Import everything within calculations

# from other import say_hi
# from calculations import multiply, fold_list, PI
# # from calculations import multiply
# import calculations

# print(__name__)  # for the system the name of this module is __main__
# print(calculations.PI)

# my_list = [2, 4]
# print(calculations.multiply(my_list))

# # Importing only the multiply function
# print(multiply([2, 4]))


# print(multiply([2, 4]))
# say_hi()


# print(PI)

# my_list = [2, 4, 5, 6, 7]
# my_list_new = []
# print(fold_list(my_list))

# for i in fold_list(my_list):
#     my_list_new.append(i * PI)
# print(my_list_new)
