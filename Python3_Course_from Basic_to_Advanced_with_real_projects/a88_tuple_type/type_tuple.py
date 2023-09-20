"""
Tuple type - An immutable list

Note: Tuples are faster than lists.

# TypeError: 'tuple' object does not support item assignment
names[1] = 'Another thing'
"""
names = ('Maria', 'Helena', 'Luiz')
# names = 'Maria', 'Helena', 'Luiz'
# names = tuple(names)
# names = list(names)

print(names[-1])
print(type(names))
print(names)
