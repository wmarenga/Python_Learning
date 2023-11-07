"""
raise - throwing exceptions (errors):

Documentation:
https://docs.python.org/3/library/exceptions.html#built-in-exceptions
"""
#! Example 1:


def not_accepted_zero(d):
    if d == 0:
        raise ZeroDivisionError('You are trying to divide by zero.')
    return True


def must_be_int_or_float(n):
    type_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" must be int or float.'
            f'"{type_n.__name__}" sent.'
        )
    return True


def divide(n, d):
    must_be_int_or_float(n)
    must_be_int_or_float(d)
    not_accepted_zero(d)
    return n / d


print(divide(8, 0))

#! Example 2


# def divide(n1, n2):
#     try:
#         return n1 / n2
#     except ZeroDivisionError as error:
#         print('Log: ', error)
#         raise


# try:
#     print(divide(2, 0))  # ZeroDivisionError: division by zero
# except ZeroDivisionError as error:
#     print(error)

#! Custom example 3:


# def divide(n1, n2):
#     if n2 == 0:
#         raise ValueError("n2 cannot be zero.")
#     return n1 / n2


# print(divide(2, 1))

# try:
#     print(divide(n1=2, n2=0))  # ValueError: n2 cannot be zero.
# except ValueError as error:
#     print('You are trying to divide by zero.')
#     print('Log: ', error)
