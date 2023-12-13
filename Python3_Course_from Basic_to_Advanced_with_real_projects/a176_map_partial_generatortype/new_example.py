# map, partial, GeneratorType e esgotamento de Iterators

from functools import partial
from types import GeneratorType


# map - to map data
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


products = [
    {'name': 'product 5', 'price': 10.00},
    {'name': 'product 1', 'price': 22.32},
    {'name': 'product 3', 'price': 10.11},
    {'name': 'product 2', 'price': 105.87},
    {'name': 'product 4', 'price': 69.90},
]


def increase_percentage(value, percentage):
    return round(value * percentage, 2)


increase_ten_percent = partial(
    increase_percentage,
    percentage=1.1
)

# new_product = [
#     {**p,
#         'price': increase_ten_percent(p['price'])}
#     for p in product
# ]


def change_product_price(product):
    return {
        **product,
        'price': increase_ten_percent(
            product['price']
        )
    }


# ? If a change the iterator for a list(), I can re-use the list().
new_products = list(map(change_product_price, products))
#                   map(    function        , iterable)
print_iter(products)
print_iter(new_products)

print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4]
    ))
)
