"""
for / else (Python):

# * Examplos:

names = ['Luiz Otávio', 'Joãozinho', 'Maria']

for n in nomes:
    print(n)
    continue  # the print below will not be executed
    print(n)

# Iterating over a list and checking
for n in names:
    # Checks if a given string starts with 'J'
    if n.startswith('J'):
        print('Begins with J', n)
    else:
        print('Does not start with J', n)


"""
# names = ['Luiz Otávio', 'Joãozinho', 'Maria']

# starts_with_j = False
# for n in names:
#     # It will work for both uppercase and lowercase letters.
#     if n.lower().startswith('j'):
#         starts_with_j = True

# if starts_with_j:
#     print('There is a word that starts with J.')
# else:
#     print('There is no word that starts with J.')

# * Another example:
for i in range(10):
    if i == 2:
        print('i is 2, jumping...')
        continue

    if i == 8:  # If we remove this "if" the for will go to the end.
        print('i is 8, your else will not execute.')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For Completed successfully!')
