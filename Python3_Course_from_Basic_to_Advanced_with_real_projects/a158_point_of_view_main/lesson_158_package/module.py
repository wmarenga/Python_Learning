"""
__all__ = ['variavel', 'sum_of_module', 'new_variable']
"""

# from lesson_158_package.module_b import say_hi # worng
from module_b import say_hi  # right

variable = 'Something'


def sum_of_module(x, y):
    return x + y


new_variable = 'OK'
say_hi()
