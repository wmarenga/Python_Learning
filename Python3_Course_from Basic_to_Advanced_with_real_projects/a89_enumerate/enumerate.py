"""
Enumerate in Python:

- Enumerate => It has the function of enumerating elements of my_list (index, value).

"""
# * Example:

my_list = ['Maria', 'Joao', 'Jose']

enumerate_list = enumerate(my_list)
# returns an iterator <enumerate object at 0x000002499710F000>
print(enumerate_list)

# for i in enumerate_list:
#     print(i)

# # ! Note: If I try to get the value again I can't,
# # ! because the enumerate already use it.

# for i in enumerate_list:
#     print(i)

# # ! Note2: If I don't assign the enumerate to a variable,
# # ! I can use it as many times as I want in the for.

# for i in enumerate(my_list):
#     print(i)

# # ! Note3: We can change the beginning of the index with enumerate.

# my_list = ['Maria', 'Joao', 'Jose']
# for i in enumerate(my_list, start=10):
#     print(i)

# # * Example of enumerate (returns tuples):

# string = 'Brazil is five stars.'
# my_list = string.split(' ')

# for index, value in enumerate(my_list):
#     # value and my_list[index] are identical
#     print(index, value, my_list[index])

# # * Example with my_list inside my_list

# my_list_2 = [[1, 'Luiz'], [3, 'João'], [5, 'Maria']]

# for index, name in my_list_2:
#     print(index, name)

# # * With enumerate:
# my_list_3 = ['Luiz', 'João', 'Maria']

# for index, name in enumerate(my_list_3):
#     print(index, name)

# # * example with unpacking:
# my_list_4 = ['Luiz', 'João', 'Maria']
# my_list_4.append('Joao')

# # for item in enumerate(my_list_4):
# #     index, value = item
# #     print(f"My index is {index} and it's value is {value}.")

# # * Example (easy way):
# for index, value in enumerate(my_list_4):
#     print(f"My index is \t{index} and \nit's value is {value}.")

# # \t => Tab
# # \n => Enter (new line)

# # * Example (using index to access directly of my_list_4.):
# for index, value in enumerate(my_list_4):
#     print(index, value, my_list_4[index])
