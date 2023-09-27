"""
Useful dictionary methods in Python:

len - quantity of keys
keys - iterable with keys
values - iterable with values
items - iterable with keys and values
setdefault - adds value if key does not exist
copy - returns a shallow copy (shallow copy)
get - get the value of a key
pop - Deletes an item with the specified key (del)
popitem - Deletes the last added item
update - Update one dictionary with another
"""
person = {
    'name': 'Luiz Otávio',
    'surname': 'Miranda',
    'age': 900,
}

# *Example => len():
# print(len(person))

# *Example => keys():
# for k in person.keys():
#     print(k)

# *Example => values():
# for v in person.values():
#     print(v)

# *Example => items():
# for i in person.items():
#     print(i, type(i))

# *Example => setdefault('keyname') default value is None:
# person.setdefault('height') # None
# person.setdefault('height', 22) # 22
# print(person)

# *Example => copy() shallow copy:
# person2 = person.copy()
# person['eyes'] = 'blue'
# print(person)
# print(person2)

# *Example => get('keyname'):
# print(person.get('name'))  # Luiz Otávio'
# print(person.get('eyes', 'Not exist'))  # 'Not exist' => standard value

# *Example => pop('keyname'):
# name = person.pop('name')
# print(name)
# print(person)

# *Example => popitem() del of last {'key':'value'}:
# last_key = person.popitem()
# print(last_key)
# print(person)

# *Example => update():
# !Note: With update() you can update an existent key:value or
# !add new key:value, if not exist.

# dogs = {
#     'dog1': 'Ruff',
#     'dog2': 'Lilica',
#     'dog3': 'Fifi',
# }
# person.update(dogs)

# print(person)
# print(dogs)

# person['height'] = 1.7
# dogs['dog4'] = 'Estopinha'
# person.update(dogs)

# print(person)
# print(dogs)

# *New way (update):
# person.update(name='new value', age='30')
# print(person)

# *another way (update) => with tuple and list:
# my_tuple = ('name', 'new value'), ('age', 30)
my_list = ('name2', 'other value'), ('age', 40)
# person.update(my_tuple)
person.update(my_list)
print(person)
