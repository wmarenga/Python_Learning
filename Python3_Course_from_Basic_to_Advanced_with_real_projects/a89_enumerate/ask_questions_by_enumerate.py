"""
Ask questions by enumerate:

"""
# internal list 0       1       2
# index 0 = ['Edu', 'João', 'Luiz']
# internal list  0        1        2
# index 1 = ['Maria', 'Aline', 'Joana']
# internal list  0       1     2
# index 2 = ['Helena', 'Ed', 'Lu']

my_list = [['Edu', 'João', 'Luiz'], [
    'Maria', 'Aline', 'Joana'], ['Helena', 'Ed', 'Lu']]

print(my_list[0][2])  # Luiz
print(my_list[1][0])  # Maria
print(my_list[2][1])  # Ed

enumerated = enumerate(my_list)
# print(enumerate)  # <class 'enumerate'>

# Doing a type casting to convert to a my_list with tuples inside.
print(list(enumerated))

# Defining the value to start with v1 (which is not the index) in the enumerate.
for v1, v2 in enumerate(my_list, 53):
    print(v1, v2)

# Unpacking:

for v1 in enumerate(my_list, 53):
    enumerated_value, my_list = v1
    name1, name2, name3 = my_list
    print(name1, name2, name3)
