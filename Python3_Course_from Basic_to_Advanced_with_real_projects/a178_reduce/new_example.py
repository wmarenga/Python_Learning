# reduce - transform an iterable into a single value
from functools import reduce

products = [
    {'name': 'product 5', 'price': 10},
    {'name': 'product 1', 'price': 22},
    {'name': 'product 3', 'price': 2},
    {'name': 'product 2', 'price': 6},
    {'name': 'product 4', 'price': 4},
]


def reduce_function(accumulator, product):
    print('accumulator', accumulator)
    print('product', product)
    print()
    return accumulator + product['price']


total = reduce(
    reduce_function,
    products,
    0
)

#! With lambda function
# total = reduce(
#     lambda ac, p: ac + p['price'],
#     products,
#     0
# )

print('The total is', total)


# total = 0
# for p in products:
#     total += p['price']

# print(total)

# print(sum([p['price'] for p in products]))
