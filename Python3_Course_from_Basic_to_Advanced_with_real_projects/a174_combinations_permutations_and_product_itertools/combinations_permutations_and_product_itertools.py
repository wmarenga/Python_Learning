"""
Combinations, Permutations and Product (Itertools):

- Combinations => the order doesn't matter;
- Permutations => the order matters;
* Both do not repeat unique values.
- Product => the order matters and repeats unique values.
"""
# #! Know all possible combinations (group of 2 people):

# from itertools import combinations, permutations, product
# from itertools import combinations, permutations
# from itertools import combinations
# people = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

# for group in combinations(people, 2):
#     print(group)

# # Luiz and André == André and Luiz, so he will ignore it (André and Luiz).

# # If the order is important, we use (permutations).

# people = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

# for group in permutations(people, 2):
#     print(group)

# #! Now both are considered (Luiz and André/ André and Luiz).
# #! However, we do not have the combinations of Luiz and Luiz, André and André, etc.

# #! To also have the values repeated with the order matters, we have to use (product).

# people = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

# for group in product(people, repeat=2):
#     print(group)

# ? Other example:

from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


people = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
t_shirt = [
    ['black', 'white'],
    ['s', 'm', 'l'],
    ['masculine', 'feminine', 'unisex'],
    ['cotton', 'polyester']
]

print_iter(combinations(people, 2))
print_iter(permutations(people, 2))
print_iter(product(*t_shirt))
