"""
- A base case that stops recursion
- factorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
https://brasilescola.uol.com.br/matematica/fatorial.htm

The recursion limit is 1000.
To change the recursion limit, we use the command below:
import sys
sys.setrecursionlimit(1004)
"""


# def recursive(start=0, end=4):
#     # import sys

#     print(start, end)
# # sys.setrecursionlimit(1004)

#     # with base
#     if start >= end:
#         return end
#     # Case recursive
#     # count at the end
#     start += 1
#     return recursive(start, end)


# print(recursive())
# # print(recursiva(0, 1001))


def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))
print(factorial(10))
print(factorial(100))
