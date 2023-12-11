"""
# Python grouping data elements (Itertools groupby):

"""
import itertools

# Create an iterator that returns consecutive keys and groups from an iterable.
numbers = [100, 90, 70, 50, 50, 100, 100, 80, 90, 80, 83, 83, 20, 20, 20]

keys = list()
groups = list()
grouped_numbers = sorted(numbers)

for k, g in itertools.groupby(grouped_numbers):
    # Adding unique elements to the keys list (ordered)
    keys.append(k)
    # adding list of repeated elements grouped in the
    # list groups (ordered)
    groups.append(list(g))
print('orderly unique elements', keys)
print('lists with equal elements grouped and ordered', groups)

#! Count of each grouped element
count_by_group = [len(i) for i in groups]
for n in range(0, len(keys)):
    print(f'The number {keys[n]} has {count_by_group[n]} elements.')

#! Using zip (dictionary with unique values: grouped numbers)
zip_values = dict(zip(keys, count_by_group))
print(zip_values)

#! Using comprehensions
mixed_letters = 'ZZDDFFFUUUooopppkkkkWWWSSSSggggg'
#! with all values separated into lists within lists
ordered_letters = sorted(mixed_letters)
print(ordered_letters)

#! List comprehension (getting only unique values => keys)
unique_values = [k for k, g in itertools.groupby(ordered_letters)]
print('Only unique values', unique_values)

#! List comprehension (grouping equal values => groups)
grouped_values = [len(list(g)) for k, g in itertools.groupby(ordered_letters)]
print(grouped_values)

for n in range(0, len(unique_values)):
    print(f'The number {unique_values[n]} has {grouped_values[n]} elements.')
