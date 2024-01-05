"""
!Recursive functions and recursion
- Functions that can call themselves back;
- Useful for breaking large problems into smaller parts;

Every recursive function must have:
- A problem that can be broken down into smaller parts;
- A recursive case that solves the small problem;
- A base case that stops recursion;
- factorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120;
https://brasilescola.uol.com.br/matematica/fatorial.htm

** Stackoverflow => The call stack is being forced to store many values
in memory.
"""


def recursive(start=0, end=4):

    print(start, end)

    # with base
    if start >= end:
        return end
    # Case recursive
    # count at the end
    start += 1
    return recursive(start, end)


print(recursive())
