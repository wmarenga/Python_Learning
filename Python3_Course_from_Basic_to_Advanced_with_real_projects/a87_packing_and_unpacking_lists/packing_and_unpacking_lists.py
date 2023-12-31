# """
# List Unpacking:

# # By using *_, we are saying that we don't need the rest of the list.
# my_list = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
# n1, n2, *_ = my_list
# print(n1, n2)

# """
# name1, name2, name3, *rest = ['Maria', 'Helena', 'Luiz']

# name, *rest = ['Maria', 'Helena', 'Luiz']
# print(rest)  # ['Helena', 'Luiz']

# # We use *_ when we create a variable that we do not intend to use.
# name, *_ = ['Maria', 'Helena', 'Luiz']
# print(_)  # ['Helena', 'Luiz']

# *_, name = ['Maria', 'Helena', 'Luiz']
# print(name, _)  # Luiz ['Maria', 'Helena']

# name1, *_, name2 = ['Maria', 'Helena', 'Luiz', 'Severino']
# print(_)  # ['Helena', 'Luiz']
# print(name2)  # ['Severino']

# name1, name2, name3, *rest = ['Maria', 'Helena', 'Luiz']
# print(rest)  # []

# my_list = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

# n1, n2, n3, *other_list, last_of_list = my_list
# print(n1, n2, n3, other_list)
# print(other_list)
# print(last_of_list)

# # O n1, n2, n3 are the third-to-last, penultimate and last elements of my_list.
# *other_list, n1, n2, n3 = my_list
# print(n1)

# Unpacking in method and function calls:

# string = 'ABCD'
# my_list = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
# my_tuple = 'Python', 'is', 'cool'
names = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# p, b, *_, u = my_list # (first and last elements = u)
# p, b, *_, ap, u = my_list  # (first and anti penultimate elements = ap)
# p, b, *_, ap, u = my_list
# print(p, u, ap)
# print(p, ap)

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*my_list) # each item separately
# print(*string) # each item separately
# print(*string. sep='-') # each item separately
# print(*my_tuple)

print(*names, sep='\n')  # The list becomes more organized.
# print(*names, end=' ') # same line
