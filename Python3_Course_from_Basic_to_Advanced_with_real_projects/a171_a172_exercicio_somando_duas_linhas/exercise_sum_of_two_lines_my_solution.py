"""
Considering two lists of integers or floats (list A and list B).
Sum the values in the lists, returning a new list with the values summed:
If one list is larger than the other, the sum will only consider the size
of the smaller one.

Example:
my_list_a     = [1, 2, 3, 4, 5, 6, 7]
my_list_b    = [1, 2, 3, 4]

*** result ***
summed_lists  = [2, 4, 6, 8]
"""
from itertools import zip_longest


my_list_a = [10, 2, 3, 4, 5]
my_list_b = [12, 2, 3, 6, 50, 60, 70]
summed_lists = [x + y for x, y in zip(my_list_a, my_list_b)]
print(summed_lists)

# Using Itertools
summed_lists2 = [x + y for x,
                 y in zip_longest(my_list_a, my_list_b, fillvalue=0)]
print(summed_lists2)
