"""
Problem with mutable parameters in Python functions.
"""
# Don't use mutable parameters as an argument of the function
# my_list=[]


def add_customers(name, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(name)
    return my_list


client1 = add_customers('luiz')
add_customers('Joana', client1)
add_customers('Fernando', client1)
client1.append('Edu')

client2 = add_customers('Helena')
add_customers('Maria', client2)

client3 = add_customers('Moreira')
add_customers('Vivi', client3)

print(client1)
print(client2)
print(client3)
