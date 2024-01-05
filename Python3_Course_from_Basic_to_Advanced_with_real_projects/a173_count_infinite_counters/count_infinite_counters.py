"""
count - Itertools (returns an iterator):

count is an endless iterator (itertools)

Generates the next function.
"""

#! Example:

from itertools import count

c1 = count(step=8, start=8)
r1 = range(8, 100, 8)

print('c1', hasattr(c1, '__iter__')) # True => an iterable (it has the __iter__ method).
print('c1', hasattr(c1, '__next__')) # True => an iterator
print('r1', hasattr(r1, '__iter__')) # True => an iterable
print('r1', hasattr(r1, '__next__')) # False (The range() method is an iterable but is not an iterator.)

print('count')
for i in c1:
    if i >= 100:
        break

    print(i)
print()
print('range')
for i in r1:
    print(i)
    
#! Example to know if it is a generator:

# from types import GeneratorType
# variable = zip('Hello', 'Hello')
# print(isinstance(variable, GeneratorType))  # False (It's not a generator)

#! For convert to a generator (with list comprehension):

# variable = ((x, y) for x, y in zip('Hello', 'Hello'))
# print(isinstance(variable, GeneratorType))  # True (Now it's a generator)

# from itertools import count
# counter = count()

# print(next(count()))
# print(next(count()))
# print(next(count()))

#! Infinite loop:

# for vHellor in counter:
#     print(vHellor)

#! The counter has a start definition:

# from itertools import count
# counter = count(start=5, step=0.05)

# for vHellor in counter:
#     print(round(vHellor, 2))

#     if vHellor >= 10:
#         break
        
#! Countdown:

# from itertools import count
# counter = count(start=9, step=-1)

# for vHellor in counter:
#     print(round(vHellor, 2))

#     if vHellor >= 10 or vHellor <= -10:
#         break

#! Generating an index for each element in the list:

# from itertools import count

# counter = count()
# # Will add new index for new elements added (automatically).
# my_list = ['Luiz', 'João', 'Maria', 'José']
# my_list = zip(counter, my_list)
# print(list(my_list))
