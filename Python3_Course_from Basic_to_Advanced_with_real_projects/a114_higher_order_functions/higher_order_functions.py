"""
Higher Order Functions => First-class functions

Higher Order Functions - Functions that can receive and/or
return other functions.

First-Class Functions - Functions that are treated like other
common data types (strings, integers, etc...).
"""


def salut(msg, name):
    return f'{msg}, {name}!'


def executes(function, *args):
    # We can use any name for "function" in executes.
    return function(*args)


print(
    executes(salut, 'Good Morning', 'Luiz')
)
print(
    executes(salut, 'Good night', 'Maria')
)
