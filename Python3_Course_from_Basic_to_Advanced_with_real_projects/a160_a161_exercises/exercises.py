# copy, sorted, products.sort

# Exercises:

import copy

from datas import products

# 1) Increase the prices of the following products by 10%.
# Generate new_products by deep copy.

new_products = [
    {**p, 'price': round(p['price'] * 1.1, 2)}
    for p in copy.deepcopy(products)
]

# print(*products, sep='\n')
# print()
# print(*new_products, sep='\n')

# 2) Sort the products by descending name (from largest to smallest).
# Generate products_ordered_by_name by deep copy.

products_ordered_by_name = sorted(
    copy.deepcopy(products),
    key=lambda p: p['name'],
    reverse=True  # False => to ascending order
)
# print(*products, sep='\n')
# print()
# print(*products_ordered_by_name, sep='\n')

# 5) Sort the products by ascending price (from lowest to highest).
# Generate ordered_products_by_price by deep copy.

products_ordered_by_price = sorted(
    copy.deepcopy(products),
    key=lambda p: p['price']
)

# FINAL

print(*products, sep='\n')
print()
print(*new_products, sep='\n')
print()
print(*products_ordered_by_name, sep='\n')
print()
print(*products_ordered_by_price, sep='\n')
