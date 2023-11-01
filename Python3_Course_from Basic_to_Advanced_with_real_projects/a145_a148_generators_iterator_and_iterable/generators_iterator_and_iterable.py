"""
generators, iterators and iterables:
The iterator has the responsibility of retaining the values while
the iterator's sole responsibility is to deliver one value at a time
(next value).
Every generator is an iterator too, but an iterator is not a generator.
The generator is a function that knows how to pause.
"""
#! Generator expression, Iterables and Iterators in Python
import sys

iterable = ['I', 'have', '__iter__']
iterator = iter(iterable)  # have __iter__ and __next__
list_comprehension = [n for n in range(1000000)]
# ? Using the parentheses, we will be creating a generator.
generator = (n for n in range(1000000))

print(sys.getsizeof(list_comprehension))  # 8448728 bites
# 104 bites (It only delivers one value at a time.)
print(sys.getsizeof(generator))

print(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

#! Shows all values in the list one by one.
# for n in generator:
#     print(n)

#! To check if the object is iterable

# import time
# import sys
# my_list = [0, 1, 2, 3, 4, 5]
# my_list1 = 1234
# my_list2 = 'String'

# print(hasattr(my_list, '__iter__'))  # True
# print(hasattr(my_list1, '__iter__'))  # False
# print(hasattr(my_list2, '__iter__'))  # True

#! Transforms the list into an iterator to display the list elements
# for v in my_list:
#     print(v)

# my_list = [0, 1, 2, 3, 4, 5]
# my_list1 = 1234
# my_list2 = 'String'

#! Making an object an iterator

# print(hasattr(my_list, '__next__'))  # False (not an iterator)
# my_list = iter(my_list)
# # Criamos o método __next__
# print(hasattr(my_list, '__next__'))  # True (not an iterator)

# print(next(my_list))  # 0
# print(next(my_list))  # 1
# print(next(my_list))  # 2
# print(next(my_list))  # 3
# print(next(my_list))  # 4
# print(next(my_list))  # 5

#! Generators
#! We use generators to optimize memory allocation

# my_list = list(range(10))  # 136 bites
# my_list = list(range(100))  # 856 bites
# my_list = list(range(1000))  # 8056 bites (8Kb)
# my_list = list(range(10000))  # 80056 bites (80Kb)

#! Check how much memory is being used for the list
# print(sys.getsizeof(my_list))

#! Wait for the entire my_list to be filled and then show
# def generates():
#     r = []
#     for n in range(100):
#         r.append(n)
#         time.sleep(0.1)
#     return r


# g = generates()

# for v in g:
#     print(v)

#! Now using generatesdores
#! The generatesdor will return one value at a time if it waits for all values to be loaded.


# def generates():
#     for n in range(100):
#         yield n
#         time.sleep(0.1)


# g = generates()

# for v in g:
#     print(v)  # Shows what is currently running

# print(hasattr(g, '__iter__'))  # generatesdores are iterable
# print(hasattr(g, '__next__'))  # generatesdores are iterators

# print(next(g))
# print(next(g))
# print(next(g))

#! Another example:

# def generates1():
#     variable = 'Value 1'
#     yield variable
#     variable = 'Value 2'
#     yield variable
#     variable = 'Value 3'
#     yield variable


# g1 = generates1()
# print(next(g1))  # Value 1
# print(next(g1))  # Value 2
# print(next(g1))  # Value 3
# print(next(g1))  # StopIteration


# my_list = [x for x in range(1000)]
# print(type(my_list))  # <class 'list'>
# print(sys.getsizeof(my_list))  # 8856 bites

#! Just changing the brackets to parentheses
# generatesdor = (x for x in range(1000))
# print(type(generatesdor))  # <class 'generator'>
# print(sys.getsizeof(generatesdor))  # 104 bites

#! Changing from 1000 to 100000
# my_list = [x for x in range(100000)]
# print(type(my_list))  # <class 'list'>
# print(sys.getsizeof(my_list))  # 800984 bites

#! Just changing the brackets to parentheses
# generatesdor = (x for x in range(100000))
# print(type(generatesdor))  # <class 'generator'>
# print(sys.getsizeof(generatesdor))  # 104 bites
