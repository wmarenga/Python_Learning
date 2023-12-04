"""
!When we use import *, we can specify what we need to import with __all__.
__all__ = [
    'variable',
    'sum_of_module',
    'new_variable',
]
"""

variable = 'something'


def sum_of_module(x, y):
    return x + y


new_variable = 'OK'
