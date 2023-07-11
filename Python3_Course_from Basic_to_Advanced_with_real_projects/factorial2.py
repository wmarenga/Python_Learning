def factorial(n):
    f = 1
    if n < 0:
        return None
    for i in range(n, 1, -1):
        f *= i
    return f


print(factorial(0))
