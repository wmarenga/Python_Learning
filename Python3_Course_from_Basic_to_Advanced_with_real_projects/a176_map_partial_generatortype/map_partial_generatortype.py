"""
The map function does not return a list, but rather an iterator of type map.
To resolve this, we must cast it to make it a list.

#! Example with lambda and list comprehension

from data import products, people, my_list

#! With lambda function
new_list = map(lambda x: x * 2, my_list)
print(list(new_list))

#! Solving in the same way with list comprehension
new_list2 = [x * 2 for x in my_list]
print(new_list2)

#! Example with dictionary

for p in products:
    print(p)

#! Defining a function that increases price


def increase_price(p):
    p['price'] = round(p['price'] * 1.05, 2)
    return p


#! Taking only the prices from the dictionary

new_products = map(increase_price, products)
# prices = map(lambda p: p['price'], products)

for product in new_products:
    print(product)

from data import products, people, my_list


def increase_age(p):
    p['new_age'] = round(p['age'] * 1.20)
    return p


# names = map(lambda p: p['name'], people)

#! We increased ages by 20%
names = map(increase_age, people)

for people in names:
    print(people)
"""
# Using more arguments within the function with map()
# Yes, but you would need a function in the middle of the way...
# Like, a function that returns another.

products = [
    {'name': 'P0', 'price': 10.23},
    {'name': 'P1', 'price': 14.65},
    {'name': 'P2', 'price': 18.56},
    {'name': 'P3', 'price': 22.23},
    {'name': 'P4', 'price': 71.87},
    {'name': 'P5', 'price': 70.03},
    {'name': 'P6', 'price': 55.12},
    {'name': 'P7', 'price': 14.56},
    {'name': 'P8', 'price': 76.65},
    {'name': 'P9', 'price': 51.32},
]


def increase_price(product, percentage):
    product['price'] = product['price'] * (1 + (percentage/100))
    return product


new_products = map(lambda product: increase_price(product, 10), products)
print(list(new_products))

#! If the lambda gets confused:

# products = [
#     {'name': 'P0', 'price': 10.23},
#     {'name': 'P1', 'price': 14.65},
#     {'name': 'P2', 'price': 18.56},
#     {'name': 'P3', 'price': 22.23},
#     {'name': 'P4', 'price': 71.87},
#     {'name': 'P5', 'price': 70.03},
#     {'name': 'P6', 'price': 55.12},
#     {'name': 'P7', 'price': 14.56},
#     {'name': 'P8', 'price': 76.65},
#     {'name': 'P9', 'price': 51.32},
# ]


# def increase_price(product, percentage):
#     product['price'] = product['price'] * (1 + (percentage/100))
#     return product


# def map_function(product):
#     return increase_price(product, 10)


# new_products = map(map_function, products)
# print(list(new_products))
