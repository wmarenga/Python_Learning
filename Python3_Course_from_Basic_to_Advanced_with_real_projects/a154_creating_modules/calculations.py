import math

PI = math.pi  # As it is a constant, we use capital letters.


def fold_list(my_list):
    return [x * 2 for x in my_list]


def multiply(my_list):
    r = 1
    for i in my_list:
        r *= i
    return r


# If the module is being imported, do not execute what is inside the if
my_list = [1, 2, 3, 4, 5]
if __name__ == '__main__':
    print(fold_list(my_list))
    print(multiply(my_list))
    print(PI)
# print(__name__)  # It is also called __main__
