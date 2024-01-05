"""
Lambda expressions (Anonymous Functions):

This function is very useful when we need to pass a function to
another function such as parameters or method of a class.
The lambda function is a function like any other in Python. Although,
are anonymous functions that contain only one line. That is, everything
must be contained within a single expression.
"""
# ! Example 1:

# def my_function(arg, arg2):
#     return arg * arg2


# var = my_function(2, 2)
# print(var)

# a = lambda x, y: x * y
# print(a(2, 2))

#! Example 2:

# my_list = [['P1', 13], ['P2', 6], ['P3', 7], ['P4', 50], ['P5', 8]]
# my_list.sort()  # It doesn't change because we have a list within another list.
# print(my_list)


# Order by product price
# def func(item):
#     return item[1]  # Order by product value.


# my_list.sort(key=func)  # Crescent
# print(my_list)
# my_list.sort(key=func, reverse=True)  # Descending
# print(my_list)

#! Example 3:

# my_list = [
#     {'name': 'Luiz', 'surname': 'miranda'},
#     {'name': 'Maria', 'surname': 'Oliveira'},
#     {'name': 'Daniel', 'surname': 'Silva'},
#     {'name': 'Eduardo', 'surname': 'Moreira'},
#     {'name': 'Aline', 'surname': 'Souza'},
# ]


# def orderby(item):
#     return item['name']


# my_list.sort(key=orderby)

# for item in my_list:
#     print(item)

#! Example 3 (with lambda):

# my_list = [
#     {'name': 'Luiz', 'surname': 'miranda'},
#     {'name': 'Maria', 'surname': 'Oliveira'},
#     {'name': 'Daniel', 'surname': 'Silva'},
#     {'name': 'Eduardo', 'surname': 'Moreira'},
#     {'name': 'Aline', 'surname': 'Souza'},
# ]

# my_list.sort(key=lambda item: item['name'])

# for item in my_list:
#     print(item)

#! Example 4:

# my_list = [['P1', 13], ['P2', 6], ['P3', 7], ['P4', 50], ['P5', 8]]

#! Example 4 (with lambda):

# my_list.sort(key=lambda item: item[1])  # Crescent
# my_list.sort(key=lambda item: item[1], reverse=True)  # Descending
# print(my_list)

# Another way to sort my_lists without changing my_list

# print(sorted(my_list, key=lambda i: i[1]))  # Crescent
# print(sorted(my_list, key=lambda i: i[1], reverse=True))  # Descending

# To sort by product name (changing the index)

# print(sorted(my_list, key=lambda i: i[0]))  # Crescent
# print(sorted(my_list, key=lambda i: i[0], reverse=True))  # Descending

# print(my_list)

#! Example 5:

# my_list = [
#     {'name': 'Luiz', 'surname': 'miranda'},
#     {'name': 'Maria', 'surname': 'Oliveira'},
#     {'name': 'Daniel', 'surname': 'Silva'},
#     {'name': 'Eduardo', 'surname': 'Moreira'},
#     {'name': 'Aline', 'surname': 'Souza'},
# ]


# def show(my_list):
#     for item in my_list:
#         print(item)
#     print()

# Use sorted to create another lists:
# l1 = sorted(my_list, key=lambda item: item['name'])
# l2 = sorted(my_list, key=lambda item: item['surname'])

# show(l1)
# show(l2)

#! Example 6:
# *args => argument NOT named.
# **kargs => argument named (with keyword).

def execute(function, *args):
    return function(*args)


def my_sum(x, y):
    return x + y

# With lambda:
# lambda x, y: x + y


def criate_mult(multiplicator):
    def mult(number):
        return number * multiplicator
    return mult


# duplicate = criate_mult(2)
duplicate = execute(
    lambda m: lambda n: n * m,
    2
)
print(duplicate(2))

print(
    execute(
        lambda x, y: x + y,
        2, 3
    ),
)

#! Example 7 (with *args):

print(
    execute(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)
