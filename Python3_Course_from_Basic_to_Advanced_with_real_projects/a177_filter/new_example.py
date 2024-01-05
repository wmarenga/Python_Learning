#! filter is a functional filter

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


def filter_price(product):
    return product['price'] > 100


# new_products = [
#     p for p in products
#     if p['price'] > 100
# ]
new_products = filter(
    # lambda product: product['price'] > 100,
    filter_price,
    products
)


print_iter(products)
print_iter(new_products)
