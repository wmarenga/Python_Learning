"""
Standard Modules in Python (import, from, as and *):

Modules are .py files that contain Python code and serve
to expand the standard functionality of the language.

See all standard Python modules in the documentation below:
https://docs.python.org/3/py-modindex.html
"""
# ?entire module - import module_name
# Advantages: You have the module namespace
# Disadvantages: big names

#! Example:
import sys

platform = 'Mine System'
print(platform)
print(sys.platform)

# ?module parts - from module_name import object1, object2
# Advantages: small names
# Desvantagens: Without the module namespace

#! Example:
# from sys import exit, platform

# print(platform)

# ? alias 1 - import module_name as nickname:

#! Example:
# import sys as s

# sys = 'something'
# print(s.platform)
# print(sys)

# ? alias 2 - from module_name import object as nickname:

#! Example:
# from sys import exit as ex
# from sys import platform as pf

# print(pf)

# Advantages: You can reserve names for your code
# Disadvantages: may be outside the language standard

#! BAD Example:
# from module_name import *

# Advantages: import everything from one module
# Disadvantages: imports everything from one module

# from sys import exit, platform

# print(platform)
# exit()

# import pymysql
# from random import randint, random
# from random import *
# from random import randint as ri_orig
# from random import randint
# import random
# from sys import platform as plat
# import sys  # the entire module
# print(sys.platform)  # win32 (operational system)

# from sys import platform  # a module object
# print(platform)  # no need to use sys

#! Example creating a nickname:

# print(plat)

#! Example with random

# for i in range(10):
#     print(random.randint(0, 10))

# for i in range(10):
#     print(randint(0, 10))

#! Example re-writing a module:


# def randint(*args):
#     return 'hahaha'


# for i in range(10):
#     print(ri_orig(0, 10))

# print(randint())

#! Example importing everything:


# for i in range(10):
#     print(randint(0, 10))

#! Example importing more objects:
# ? The random.random function generates a random number between 0 and 1 (float).


# for i in range(10):
#     print(randint(0, 10), random())

#! Installing non-native Python modules:
# ? pip install mysqlclient

#! Uninstalling a module
# ? pip uninstall pymysql
