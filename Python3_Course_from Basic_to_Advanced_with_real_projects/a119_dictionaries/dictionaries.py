"""
Python dictionaries {key: value} => (dict type):

- Dictionaries are data structures of type "key" and "value" pair.
- Keys can be considered as the "index" that we saw in the list
and can be of immutable types such as: str, int, float, bool, tuple, etc.
- Keys in a dictionary must be unique.
- The value can be of any type, including another dictionary.
- We use the braces - {} - or the dict class to create dictionaries.
- Dictionaries are similar to lists,they have (key/index and value),
however in dictionaries, we can change the values of the keys. In lists,
indexing is automatic and we cannot change the index.

> Immutable: str, int, float, bool, tuple
> Mutable: dict, list

Data types in keys:
- 'str': 'value'
- 123: 'Other value'
- (1, 2, 3, 4): 'tuple'
"""
# *Example 1:

# person = {
#     'name': 'Luiz Otávio',
#     'surname': 'Miranda',
#     'age': 18,
#     'height': 1.8,
#     'address': [
#         {'street': 'tal tal', 'number': 123},
#         {'street': 'other street', 'number': 321},
#     ]
# }

# !Other way:
# person = dict(name='Luiz Otávio', surname='Miranda')

import os
import copy
# person = {
#     'name': 'Luiz Otávio',
#     'surname': 'Miranda',
#     'age': 18,
#     'height': 1.8,
#     'address': [
#         {'street': 'tal tal', 'number': 123},
#         {'street': 'other street', 'number': 321},
#     ],
# }
# # print(person, type(person))
# print(person['name'])
# print(person['surname'])

# print()

# for key in person:
#     print(key, person[key])

# *Example 2:
# d1 = {'key1': 'key value'}
# print(d1)

# ?Adding a new key:
# d1['new key'] = 'value of the new key'
# print(d1)

# ?Accessing a key in the dictionary:
# print(d1['key1'])

# ?Another way to create a dictionary (with cast):
# d2 = dict(name='Wellington', age='51', height=1.70)
# print(d2)

# ?duplicate keys
# ?Only the last key will be created, as they are duplicates.
# d1 = {'key': 'value', 'key': 'abc', 'key': 'real value of the key'}
# print(d1)

# d2 = {'str': 'value', 123: 'other value', (1, 2, 3, 4): 'tuple'}
# print(d2[(1, 2, 3, 4)])  # tuple

# print(d2['not exist'])  # KeyError

# ?Getting around this error
# if 'not exist' in d2:
#     print(d2['not exist'])
# else:
#     d2['not exist'] = 'now exist'

# print(d2)

# ?Another way around with get() => returns None if the key does not exist:
# ?This way the code doesn't stop working.
# d2 = {'str': 'value', 123: 'other value', (1, 2, 3, 4): 'tuple'}
# print(d2.get('keyname'))  # None

# if d2.get('keyname') is not None:
#     print(d2.get('keyname'))
# else:
#     d2['keyname'] = 'Now exist'

# print(d2)

# ?Changing an existing key:
# d2['str'] = 'Ruff'
# print(d2)

# ?Another way to change a {key: value}:
# d2.update({'new_key': 'new_value'})
# print(d2)

# d2.update({'str': 'Renata'})
# print(d2)

# ?Deleting key from the dictionary:
# d2 = {'str': 'value', 123: 'other value', (1, 2, 3, 4): 'tuple'}
# print(d2)

# del(d2['str'])
# print(d2)

# print('str' in d2)  # Checking by key
# print('value' in d2.keys())  # Checking by key

# print('value' in d2.values())  # Checking by value

# ?Check how many {key:value} pairs there are:
# print(len(d2))

# ?Iterating over a dictionary:
# d2 = {'key1': 'value', 'key2': 'ther value', 'key3': 'tuple'}

# ?Accessing by keys (keys):
# for k in d2.keys():
#     print(k)

# ?Accessing by values (values):
# for v in d2.values():
#     print(v)

# ?Accessing by the set key:value (items):
# ?Returns tuples
# for i in d2.items():
#     print(i)
#     print(i[0], i[1])  # key and value separately

# d2 = {'key1': 'value', 'key2': 'other value', 'key3': 'tuple'}

# ?Unpacking dictionaries:
# for k, v in d2.items():
#     print(k, v)

# ?Creating a list with dictionary elements (key: value):
# my_list = list()
# for k, v in d2.items():
#     my_list.append(k)
#     my_list.append(v)

# print(my_list)

# ?Dictionaries within dictionaries:
# clients = {
#     'client1': {
#         'name': 'Luiz',
#         'surname': 'Otávio',
#     },
#     'client2': {
#         'name': 'João',
#         'surname': 'Moreira',
#     },
#     'client3': {
#         'name': 'Maria',
#         'surname': 'Moreira',
#     }
# }

# ?The first for takes the external values,
# ?and thesecond for takes the internal dictionaries.
# for clients_k, clients_v in clients.items():
#     print(f'Displaying {clients_k}')
#     for data_k, data_v in clients_v.items():
#         print(f'\t{data_k} = {data_v}')  # \t is to tab (indent)

# ?When we determine that a variable receives another variable,
# ?both will be changed. We do not create a copy, but rather
# ?associate them, pointing both to the same memory space.
# d3 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Luiz', 'Otávio']}
# v = d3
# print(v)
# print(d3)

# v[1] = 'Luiz'  # We are changing v and d3.
# print(v)
# print(d3)

# !Creating a shallow copy:
# d3 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Luiz', 'Otávio']}
# v = d3.copy()
# v[1] = 'Oi'
# print(d3)
# print(v)

# ?Accessing an element of a my_list within a dictionary value:
# print(v['d'][0])

# ?Changing the value
# v['d'][0] = 'Joãozinho'
# print(d3)
# print(v)

# ?Deepcopy creates an independent copy
# d3 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Luiz', 'Otávio']}
# v = copy.deepcopy(d3)

# v[1] = 'Luiz'
# v['d'][0] = 'Joãozinho'

# print(d3)
# print(v)

# ?Casting my_lists or tuples to a dictionary (by similarity):


# def clean():
#     os.system('cls')


# clean()

# my_list = [
#     ['c1', 1],
#     ['c2', 2],
#     ['c3', 3],
# ]

# d1 = dict(my_list)
# print(d1)

# ?Deleting the last key:value from a dictionary (pop())
# d2 = {
#     1: 2,
#     2: 3,
#     4: 5,
# }
# d2.pop(4)  # Deleting key 4
# d2.popitem()  # Deletes the last item regardless of what it is.

# ?Concatenating 2 dictionaries

# d5 = {
#     'a': 'b',
#     'c': 'd',
# }

# print(d5)

# d2.update(d5)  # Will include d5 in d2 (concatenating the 2)
# print(d2)
