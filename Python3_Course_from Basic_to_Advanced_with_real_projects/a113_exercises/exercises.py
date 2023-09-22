
# *Exercise 1:

"""
Create a function that displays a greeting with the greeting and
name parameters.
"""


# def salut(salut='Hello!', name='User'):
#     return f'{salut} {name.capitalize()}! Welcome to the system.'


# print(salut('Hello', 'Wellington'))

# *Exercise 2:

"""
Create a function that takes 3 numbers as parameters
and displays the sum between them.
"""


# def sum3(n1, n2, n3):
#     return n1 + n2 + n3


# print(sum3(33, 66, 99))

# *Exercise 3:

"""
Create a function that takes 2 numbers. The first is a
value and the second a percentage (ex. 10%). Return the
value of the first number plus its percentage increase.
"""


# def percent(n1, perc):
#     return f"More {perc}% of {n1} is {n1 + (n1 * (perc / 100))}"


# print(percent(50, 10))


# *Exercise 4:

"""
Create a function that multiplies all incoming unnamed arguments.
Return the total for a variable and output the variable's value.

! Note: Multiplication by zero is always zero.
"""
# ?Example 1:

# import numpy

# def my_mult(*args):
#     total = numpy.prod(args)
#     return total


# my_numbers = [1, 2, 3, 4, 5, 6, 7]
# print(my_mult(*my_numbers))

# ?Example 2:

# def my_mult(*args):
#     total = 1
#     for num in args:
#         total *= num
#     return total


# multiplication = my_mult(10, 2, 3, 4, 5)
# print(multiplication)

# *Exercise 5:

"""
Create a function that tells you whether the number is even or odd.
Return whether the number is even or odd.
"""

# ?Example 1:


# def even_odd(num):
#     if num % 2 == 0:
#         return f"The number {num} is EVEN."
#     return f"The number {num} is ODD."


# print(even_odd(3))

# ?Example 2:


# def even_odd2(num):
#     two_numbers_multi = num % 2 == 0

#     if two_numbers_multi:
#         return f'{num} is EVEN'
#     return f'{num} is ODD'


# other_even_odd = even_odd2
# two_is_even = other_even_odd(2)
# print(two_is_even)
# print(even_odd2(3))
# print(even_odd2(15))
# print(even_odd2(16))

# print(even_odd2 is other_even_odd)

# *Exercise 6:

"""
Fizz Buzz - If the function parameter is divisible by 3, return fizz,
if the function parameter is divisible by 5, return buzz. If the
function parameter is divisible by 5 and 3, return FizzBuzz,
otherwise, return the number sent.
"""

# from random import randint


# def fb(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return f'fizzbuzz, {n} is divisible by 3 and 5'
#     if n % 5 == 0:
#         return f'buzz, {n} is divisible by 5'
#     if n % 3 == 0:
#         return f'fizz, {n} is divisible by 3'
#     return n

"""
print(fizzbuzz(7))
print(fizzbuzz(10))
print(fizzbuzz(15))
print(fizzbuzz(22))

"""

# for i in range(100):
#     randomized = randint(0, 100)
#     print(fb(randomized))

# *Exercise 7:

"""
Create a function1 that takes a function2 as a
parameter and returns the value of the executed function2.
"""


# def function1(function2):
#     return function2


# def function2():
#     variable = 'Wellington'
#     return variable


# function2 = function2()
# print(function1(function2))

# *Exercise 8:

"""
Create a function1 that takes a function2 as a parameter
and returns the value of the executed function2.
"""


# def hello_world(master):
#     return master


# def master():
#     return 'Hello2'


# print(master())

# *Exercise 9:

"""
Create a function1 that takes a function2 as a parameter
and returns the value of the executed function2. Make
function1 execute two functions that take a number
different from arguments.
"""


def master(function, *args, **kwargs):
    return function(*args, **kwargs)


def say_hi(name):
    return f'Hello {name}'


def salut(name, salut):
    return f'{salut} {name}'


exec1 = master(say_hi, 'Luiz')
exec2 = master(salut, 'Luiz', salut='Good Morning!')
print(exec1)
print(exec2)
