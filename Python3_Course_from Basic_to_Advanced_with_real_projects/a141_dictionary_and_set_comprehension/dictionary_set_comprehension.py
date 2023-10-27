# Dictionary Comprehension:

#! Example 1:
import random
my_list = [
    ('key1', 'value1'),
    ('key2', 'value2')
]

# d1 = dict(my_list) with cast
d1 = {x: y for x, y in my_list}  # without cast
print(d1)

d2 = {x: y * 2 for x, y in my_list}
print(d2)

#! Example 2:
my_list = [
    ('key1', 2),
    ('key2', 9)
]
d1 = dict(my_list)  # with cast
d3 = {x: y * 2 for x, y in my_list}
print(d3)

#! Example 3:
my_list = [
    ('key1', 'value1'),
    ('key2', 'value2')
]
d4 = {x.upper(): y.upper() * 2 for x, y in my_list}
print(d4)

#! Example 4

d5 = {x: y for x in range(5) for y in random.choice('asdfgbvbnnhh')}
print(d5)

#! Example 5:

d6 = {f'key_{x}': x ** 2 for x in range(5)}
print(d6)

#! Example 6:

product = {
    'name': 'blue pen',
    'price': 2.5,
    'category': 'office',
}

dc = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value
    in product.items()
    if key != 'category'
}

my_list = [
    ('a', 'value a'),
    ('b', 'value a'),
    ('b', 'value a'),
]
dc = {
    key: value
    for key, value in my_list
}

s1 = {2 ** i for i in range(10)}
print(s1)

#! Set Comprehension:

s1 = {2 ** i for i in range(10)}
print(s1)
