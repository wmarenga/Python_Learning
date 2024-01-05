"""
Exercise - Lists union:

Create a zipper function (like the clothes zipper).
The job of this function will be to join two lists in order.
Use all values from the shortest list.

Ex.:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']

Result
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
"""


# def zipper(first_list, second_list):
#     interval = min(len(first_list), len(second_list))
#     return [
#         (first_list[i], second_list[i]) for i in range(interval)
#     ]


from itertools import zip_longest
brasilian_cities = ['Salvador', 'Ubatuba', 'Belo Horizonte']
cities_abreviations = ['BA', 'SP', 'MG', 'RJ']

# print(zipper(brasilian_cities, cities_abreviations))

# Using zip function:
print(list(zip(brasilian_cities, cities_abreviations)))

# Using zip_longest, we get de value of bigger list.
print(list(zip_longest(brasilian_cities,
      cities_abreviations, fillvalue="No city name")))
