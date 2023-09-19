"""
Exercise
Display the indexes of the list
0 Maria
1 Helena
2 Luiz
"""
my_list = ['Maria', 'Helena', 'Luiz']
my_list.append('João')
index = []

# indexes = range(len(my_list))

# for index in indexes:
#     print(index, my_list[index], type(my_list[index]))

for i in range(0, len(my_list)):
    print(i, my_list[i])
