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
my_list_a = [10, 2, 3, 40, 5, 6, 7]
my_list_b = [1, 2, 3, 4]
summed_lists = [x + y for x, y in zip(my_list_a, my_list_a)]

# Creates a list of tuples with the values of my_list_a and my_list_b.
# print(list(zip(my_list_a, my_list_b)))
print(summed_lists)

# summed_lists = []
# get the indexes from the smaller list.

# for i in range(len(my_list_b)):
#     summed_lists.append(my_list_a[i] + my_list_b[i])
# print(summed_lists)

# summed_lists = []

# Using _ we omit the value of enumerate
# for i, _ in enumerate(my_list_b):
#     summed_lists.append(my_list_a[i] + my_list_b[i])
# print(summed_lists)
"""
The problem is that zip only joins the lists up to the size of the
smallest list (as proposed in the exercise).

Another possibility is to use zip_longest to capture the values
from the longer list.

The idea is the same, see:
"""

my_list_a = [10, 2, 3, 4, 5]
my_list_b = [12, 2, 3, 6, 50, 60, 70]
summed_lists = [x + y for x,
                y in zip_longest(my_list_a, my_list_b, fillvalue=0)]
print(summed_lists)  # [22, 4, 6, 10, 55, 60, 70]

# In this case, we use the "fillvalue" as 0 (zero), so we can
# capture the remaining values from the larger list, performing
# calculations, without getting an error in our program (infinite loop).
