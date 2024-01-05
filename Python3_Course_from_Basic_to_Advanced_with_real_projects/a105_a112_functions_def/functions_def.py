"""
Functions (def) in Python:

Introduction to functions (def) in Python.
Functions are snippets of code used to replicate
a certain action throughout your code. They can
receive values for parameters (arguments) and return
a specific value. By default, Python functions return None.

"""
# *Example 1:


# def show1(a, b, c):
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')


# def show(a, b, c):
#     print(a, b, c)


# show1(1, 2, 3)
# show1(4, 5, 6)


# *Example 2 (Normal):


# def salut(msg, name):
#     return msg, name


# print(salut('Hello!', 'Wellington'))

"""
Named and unnamed arguments in Python functions.
Named argument has name with equals sign.
Unnamed argument takes only the argument (value).
"""
# *Example 3 (Named argument):
# !Note1: If we try to print a function that returns a print,
# ! None will appear (redundant print).

# ! Note2: The function parameters are positional. If we want
# ! to specify the arguments for each parameter, we have to
# ! name the arguments in the function call => add(x=1, y=2, z=3).

# ! Note3: If we name an argument, all subsequent arguments must
# ! be named. The same rule applies to the parameter.


# def add(x, y, z):
#     # Definition
#     print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


# add(1, 2, 3)
# add(1, y=2, z=5)

# print(1, 2, 3, sep='-')

"""
Default values for parameter:
When defining a function, parameters can have default values.
If the value is not sent for the parameter, the default value will be used.
Refactor: edit your code.
"""

# *Example 4 (Named argument):


# def add(x, y, z=None):
#     if z is not None:
#         print(f'{x=} {y=} {z=}', x + y + z)
#     else:
#         print(f'{x=} {y=}', x + y)


# add(1, 2)
# add(3, 5)
# add(100, 200)
# add(7, 9, 0)  # positional
# add(y=9, z=0, x=7)  # named

# *Example 5 (Using default value):

# def salut(msg='Hello!', name='User'):
#     return msg, name


# print(salut())

# *Example 6 (Using default value):

# def salut(name='No name'):
#     print(f'Hello, {name}!')

# salut('Luiz Otávio')
# salut('Maria')
# salut('Helena')
# salut()

# *Example 7 (Using default value):
# We can invert when parameters are named.

# def salut(msg='Hello!', name='User'):
#     return msg, name


# print(salut(name='Zezinho', msg='Hi'))

# *Example 8 (using replace()):


# def salut(msg='Hello ', name='User!'):
#     name = name.replace('e', '3')
#     msg = msg.replace('i', 'o')
#     return f'{msg} {name}'


# print(salut(name='Zezinho', msg='Hi'))

# *Example 9 (return)

# !Note: Return of function values (return) and exit function.


# def add(x, y):
#     if x > 10:
#         return [10, 20]
#     return x + y


# # variable = add(1, 2)
# # variable = int('1')
# add1 = add(2, 2)
# add2 = add(3, 3)
# print(add1)
# print(add2)
# print(add(11, 55))

# *Example 10
# ! Note: After return nothing will appear.

# def function(var):
#     return var
#     print('This will not executed.')


# variable = function('Value I want.')
# print(variable)  # None (no value)

# if variable:
#     print(variable)
# else:
#     print('No value.')

# *Example 11 (DivisionError)
# ! Note: Divisions by zero are not allowed in mathematics.


# def division(n1, n2):
#     if n2 > 0:
#         return n1 / n2
#     else:
#         return 'Invalid count.'


# divide = division(8, 2)  # (n1=8, n2=2)
# print(divide)

# divide = division(8, 0)  # DivisionError
# print(divide)

# *Example 12 (A function calling another function.)


# def f(var):
#     print(var)


# def dumb():
#     return f


# var = dumb()
# print(var, type(var))

# print(type(f))

# var = dumb()('And put my value here.')
# print(var)
# print(type(var))

# # Checking the variable memory id()
# var = dumb()
# print(id(var), id(f))

# if var == f:
#     print("var is equal to f.")
# else:
#     print('Blaaaaaaa')

# ! Using *args, **kwargs:
# !Note1 (*args) => unnamed arguments (sequential arguments).
# !Note2 (**kwargs) => Keyword arguments (named arguments).
# !Note3 => The names args and kwargs are just a convention.
# ! The important thing is the asterisks (* and **).

# When I define a default (named) parameter, the
# next ones must be named as well.

"""
args - Unnamed arguments
* - *args (packing and unpacking)

Remember about unpacking concept
x, y, *rest = 1, 2, 3, 4
print(x, y, rest)

! Converting args to a list.
args = list(args)
"""

# *Example 13


# def add(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total


# print(add(1, 2, 3, 4, 5, 6))

# *Example 14

# def add(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total


# add_1_2_3 = add(1, 2, 3)
# # print(add_1_2_3)

# add_4_5_6 = add(4, 5, 6)
# # print(add_4_5_6)

# nums = 1, 2, 3, 4, 5, 6, 7, 78, 10
# other_add = add(*nums)
# print(other_add)

# print(sum(nums))
# # print(*nums)

# *Example 15

# def add(*args):
#     return sum(args)


# my_list = [1, 2, 3, 4, 5, 6, 7]

# print(add(*my_list))

# *Example 16


# def func(a1, a2, a3, a4, a5, name=None, a6=None):
#     print(a1, a2, a3, a4, a5, name)
#     return name, a6


# func(1, 2, 3, 4, 5)
# var = func(1, 2, 3, 4, 5, name='Luiz', a6='5')
# print(var[0], var[1])


# def func(*args):
#     print(args)

# *Example 17 with *args (returns a tuple):


# def func(*args):
#     args = list(args)  # Cast the tuple values to list.
#     args[0] = 20
#     print(args)
#     # print(args[0])  # Same list principle (first element).
#     # print(args[-1])  # Same list principle (last element).
#     # print(len(args))


# func(1, 2, 3, 4, 5)

# my_list = [1, 2, 3, 4, 5, 6]
# # n1, n2, *n = my_list  # Unpacking
# # print(n1, n2, n)  # Showing n1, n2 and the rest of my_list.
# # print(*my_list, sep='-')  # Displays the unpacked my_list values.

# # Sending the unpacked my_list


# def func2(*args):
#     print(args)


# # The two my_list will be concatenated into a single tuple.
# my_list = [1, 2, 3, 4, 5]
# my_list2 = [10, 20, 30, 40, 50]
# func2(*my_list, *my_list2)

# *Example 18 (Using args/ kwargs)


# def func3(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     print(kwargs['name'], kwargs['surname'])

#     # The best thing is to use get() when we don't know if it exists.
#     name = kwargs.get('name')
#     print(name)

#     age = kwargs.get('age')  # None, because I didn't say my age.
#     print(age)

#     if age is not None:
#         print(age)
#     else:
#         print('age not exist.')

#     age = kwargs['age']  # KeyError if the age is not informed.


# my_list = [1, 2, 3, 4, 5]
# my_list2 = [10, 20, 30, 40, 50]
# func3(*my_list, *my_list2, name='Luiz', surname='Miranda', age=30)

# !Scope of variables (Local and Global):

"""
Scope of Functions in Python:

Scope means where that code can reach.
There is global and local scope.
The global scope is the scope where all code is reachable.
The local scope is the scope where only names from the same location can be reached.
We do not have access to internal scope names in external scopes.
The word global makes a variable in the outer scope the same in the inner scope.
flow => internal function to external function(s)

Call stack (temporary memory allocation) => The call stack is a language interpreter mechanism that organizes
how the script works when many functions are called, which function is currently
being executed, and which ones will be called within a function, etc.
"""
# *Example 19 (Global scope):

# Global scope:
# variable = 'value'
# print(variable)


# def func():
#     print(variable)


# def func2():
#     global variable  # We are determining that this variable will be global
#     variable = 'Other value'
#     print(variable)


# func()
# func2()

# print(variable)  # This variable will display 'value' as it is showing
# # the global variable.

# *Example 20 (Global scope):

# x = 1


# def global_scope():
#     global x
#     x = 10

#     def other_function():
#         global x
#         x = 11
#         y = 2
#         print(x, y)

#     other_function()
#     print(x)


# print(x)
# global_scope()
# print(x)

# *Example 21

# variable = 'value2'


# def func1():
#     other_variable = 'value func1()'
#     # print(variable)  # UnboundLocalError
#     # variable = 1234  # local variable
#     # print(variable)


# def func2():
#     print(other_variable)  # We cannot access it, as it is
#     # a local variable of another function.


# func1()
# func2()  # NameError

# # To solve this problem

# *Example 22


# def func1():
#     other_variable = 'Wellington'
#     return other_variable


# def func2(arg):
#     print(arg)


# var = func1()
# func2(var)
