# Introduction to Generator functions in Python

# generator = (n for n in range(1000000))


# def generator(n=0):
#     yield 1  # pause
#     print('Continue...')
#     yield 2  # pause
#     print('Again...')
#     yield 3  # pause
#     print('Almost finished...')
#     return "It's over..."


# gen = generator(n=0)
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))

# #! Using for:
# for n in gen:
#     print(n)

# def generator(n=0, maximum=10):
#     while True:
#         yield n  # pause in n=0
#         n += 1

#         if n >= maximum:
#             return


# gen = generator(maximum=1000000)
# for n in gen:
#     print(n)

#! Yield from

#! Example 1:

# def gen1():
#     yield 1
#     yield 2
#     yield 3


# def gen2():
#     yield from gen1()
#     yield 4
#     yield 5
#     yield 6


# g = gen2()
# for number in g:
#     print(number)

#! Example 2:

def gen1():
    print('Started GEN1')
    yield 1
    yield 2
    yield 3
    print("It's over GEN1")


def gen3():
    print('Started GEN3')
    yield 10
    yield 20
    yield 30
    print("It's over GEN3")


def gen2(gen=None):
    print('Started GEN2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print("It's over GEN2")


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for number in g1:
    print(number)
print()
for number in g2:
    print(number)
print()
for number in g3:
    print(number)
print()

#! Behavior of Generators and Iterators.
#! list, tuple, str => Sequences => Iterables

# name = 'Luiz Otávio'

# for letter in name:
#     print(letter)

# print('#' * 80)

# for letter in name:
#     print(letter)

#! On the contrary an iterable, the generator runs until the end and is finished.
#! Generators are iterable and are also iterators.

# name = 'Luiz Otávio'
# iterator = iter(name)
# generator = (letter for letter in name)

#! Example with generator:

# print(next(generator))  # L
# print(next(generator))  # u
# print(next(generator))  # i
# print(next(generator))  # z

#! From here it will consume the rest of the generator (with for).
# print('Consuming the rest with for:')

# for letter in generator:
#     print(letter)

# print('Look, the other one is worthless: ')

# for letter in generator:
#     print(letter)
# print('############################')

#! Example with iterator:

# try:
#     print(next(iterator))  # L
#     print(next(iterator))  # u
#     print(next(iterator))  # i
#     print(next(iterator))  # z
#     print(next(iterator))  # space
#     print(next(iterator))  # O
#     print(next(iterator))  # t
#     print(next(iterator))  # á
#     print(next(iterator))  # v
#     print(next(iterator))  # i
#     print(next(iterator))  # o
#     print(next(iterator))  # StopIteration
# except:
#     pass

# print(next(iterator))  # StopIteration

#! We have exhausted all iterations (all iterations have been used).
