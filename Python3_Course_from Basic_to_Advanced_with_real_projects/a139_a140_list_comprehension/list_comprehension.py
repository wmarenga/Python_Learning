"""
List Comprehension:
"""
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#! Example 1:
# ex1 = [variable for variable in l1]
# print(ex1)

#! Example 2:
# ex2 = [v * 2 for v in l1]
# print(ex2)

#! Example 3:
# ex3 = [(v, v2) for v in l1 for v2 in range(3)]
# print(ex3)

#! Exemplo 4:
# l2 = ['Luiz', 'Mauro', 'Maria']
# ex4 = [v.replace('a', '@') for v in l2]
# print(ex4)

#! Example 5:
# tupla = (
#     ('key1', 'value'),
#     ('key2', 'value2')
# )
# ex5 = [(y, x) for x, y in tupla]
# ex5 = dict(ex5)  # cast for a dictionary
# print(ex5)
# print(ex5['value2'])

#! Example 6:
# l3 = list(range(100))

# # Numbers divisible by 2
# ex6 = [v for v in l3 if v % 2 == 0]
# print(ex6)

# # Numbers divisible by 3 and 8
# ex6 = [v for v in l3 if v % 3 == 0 and v % 8 == 0]
# print(ex6)

#! Example 7 (using else):

# l3 = list(range(100))
# ex7 = [v if v % 3 == 0 and v % 8 == 0 else '-' for v in l3]
# print(ex7)

#! Example 8:

# my_list = []

# for x in range(3):
#     for y in range(3):
#         my_list.append((x, y))
# my_list = [
#     (x, y)
#     for x in range(3)
#     for y in range(3)
# ]
# my_list = [
#     [(x, letter) for letter in 'Luiz']
#     for x in range(3)
# ]

# print(my_list)

#! Example 9:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# new_numbers = [number for number in numbers if number > 5]
# even_numbers = [number for number in numbers if number % 2 == 0]
# odd_numbers = [number for number in numbers if number % 2 != 0]
# another_if = [number if number !=
#               6 else 600 for number in numbers if number % 2 == 0]

# another_if2 = [number if number !=
#                6 else 600 for number in even_numbers]

# print(numbers)
# print(new_numbers)
# print(even_numbers)
# print(odd_numbers)
# print(another_if)
# print(another_if2)

#! Example 10:

line_column = [
    (x, y)
    if y != 2 else (x, y * 1000)
    for x in range(1, 11)
    for y in range(1, 6)
    if x != 2
]

print(line_column)
