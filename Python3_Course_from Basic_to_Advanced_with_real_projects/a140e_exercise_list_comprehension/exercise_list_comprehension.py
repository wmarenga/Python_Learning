"""
Exercise List Comprehension:

Use list comprehension (one line of code)

shopping_cart = []
shopping_cart.append(('product 1', 30))
shopping_cart.append(('product 2', 20))
shopping_cart.append(('product 3', 50))

total = []
for product in shopping_cart:
    total.append(product[1])
print(sum(total))
"""

shopping_cart = []
shopping_cart.append(('product 1', 30))
shopping_cart.append(('product 2', 20))
shopping_cart.append(('product 3', 50))

print(sum([p[1] for p in shopping_cart]))

# Teacher's solution

total = [(x, y) for x, y in shopping_cart]  # unpacking the values
print(total)

# Taking the prices in y
total = [(y) for x, y in shopping_cart]  # unpacking the values
print(total)

# Converting all values to float and doing the sum
total = sum([float(y) for x, y in shopping_cart])  # unpacking the values
print(total)
