"""
sets => represents sets (mathematics) - type set:

- Graphically represented by the Venn diagram;
- Sets in Python are mutable, but they only accept immutable types as internal values;
- Sets are similar to dictionaries, but they do not have keys and indexes;
- Sets like tuples are immutable;
- Sets have no ordering;
- Sets do not accept repetitions of values;
- Sets are efficient for removing duplicate values from iterables;
- Do not accept mutable values;
- Your values will always be unique;
- Sets have no indexes;
- Sets have no order;
- They are iterable (for, in, not in)

Most common methods:
add                      => add elements
update                   => update values
clear                    => clears all values
discard                  => removing elements

Useful operators:
set.union (|)            => joins
intersection (&)         => all elements present in both sets
difference (-)           => elements only in the left set (pay attention to the order of the sets)
symmetric_difference (^) => elements that are in both sets, but not both.
"""
# *Example 1:
# s1 = {1, 2, 3, 4, 5}
# print(s1)

# *Example 2 (creating a set):
# iterable = 'Wellington'
# print(set(iterable))  # No order {'l', 'W', 'g', 'o', 't', 'i', 'n', 'e'}
# print({'Wellington'})  # {'Wellington'}
# s1 = set('Luiz')
# s1 = set()  # empty
# s1 = {'Luiz', 1, 2, 3}  # with datas

# *Example 3:
letters = set()
while True:
    letter = input('Type a letter: ')
    letters.add(letter.lower())

    if 'l' in letters:
        print(f"You typed the following letters {letters}.")
        print('Congrats!')
        break

    print(letters)

# ?We can iterate over the values with for, but not directly (via indices):
# for v in s1:
#     print(v)

# ?We can add to a list:
# my_list = []
# for v in s1:
#     my_list.append(v)
# print(my_list)

# ?Creating empty sets with cast:
# s2 = set()

# ?Inserting values into the set:
# s2.add(1)
# s2.add(2)
# # s2.add((1, 2, 3, 'Luiz'))
# print(s2)

# !Note: Mutable values cannot be inserted into the set (list, dictionary, set).
# list_in_set = {1, 2, 3, [1, 2, 3]}  # TypeError: unhashable type: 'list'
# set_in_set = {1, 2, 3, {1, 2, 3}}  # TypeError: unhashable type: 'set'
# tuple_in_set = {1, 2, 3, (1, )}  # OK
# dictionary_in_set = {1, 2, 3, {'name': 'Wellington'}} # TypeError: unhashable type: 'dict'

# ?Removing elements:
# s2.discard(2)
# print(s2)

# ?update
# s1 = set()
# s1.update('Python')
# # No duplicate values
# s1.update([1, 2, 3, 4, 5], {5, 6, 7, 8})  # {1, 2, 3, 4, 5, 6, 7, 8}
# print(s1)  # all letters will be inserted separately and without order

# ?Eliminating duplicate elements:
# l1 = [1, 2, 2, 1, 1, 3, 4, 4, 6, 6, 7, 8, 9, 9, 'Luiz', 'Luiz']
# l1 = set(l1)
# print(l1)

# ?Casting to convert to list again:
# l1 = list(l1)  # Elements may return out of order.
# print(l1)

# ?union (|)
# s1 = {1, 2, 3, 4, 5}
# s2 = {5, 5, 6, 7, 8, 9}  # add without repetitions
# s4 = {'a', 'b', 'c'}
# # s3 = s1 | s2
# s3 = s1.union(s2, s4)
# print(s3)

# ?intersection (&)
# s1 = {1, 2, 6, 4, 5, 'b'}
# s2 = {5, 6, 7, 8, 9, 'a'}
# s3 = {'a', 'b', 'c', 5, 6}
# # s4 = s2.intersection(s1, s3)  # {5}
# s4 = s1 & s2 & s3
# print(s4)

# ?difference (-)
# !Note: Everything that belongs to the first set except the
# !elements that are in both sets.
# s1 = {1, 2, 6, 4, 5, 'b'}
# s2 = {5, 6, 7, 8, 9, 'a'}
# s3 = {'a', 'b', 'c', 5, 6}

# s4 = s1 - s2
# s4 = s1.difference(s2)
# print(s4)


# ?symmetric_difference (^)
# !Note: Everything that is not the same in both. Union minus intersession.
# s1 = {1, 2, 6, 4, 5, 'b'}
# s2 = {5, 6, 7, 8, 9, 'a'}
# s3 = {'a', 'b', 'c', 5, 6}
# s4 = s2 ^ s1
# print(s4)
# s5 = (s1 | s2) - (s1 & s2)
# print(s5)
