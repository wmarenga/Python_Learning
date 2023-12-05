"""
Decorative Functions:

Decorator functions involve a method changing or
not changing the behavior of the function or class.
We use decorators to add extra functionality to
other functions or classes.

def say_hi():
    print('Hello!')


# say_hi()

# Throwing a function into a variable
variable = say_hi

variable()
print(type(variable))  # <class 'function'>


def master(my_function):
    def slave(*args, **kwargs):
        print('Now I'm decorated.')
        my_function(*args, **kwargs)
    return slave  # returns the function without executing


@master
def say_hi():
    print('Hello!')


@master
def other_function(msg):
    print(msg)


# say_hi = master(say_hi)
# say_hi()
# print(type(say_hi))  # <class 'function'>

other_function('Hello,I am Wellington.')
"""
from time import time
from time import sleep


def speed(my_function):
    def internal_function(*args, **kwargs):
        start_time = time()
        result = my_function(*args, **kwargs)
        end_time = time()
        # Time in milliseconds
        my_time = (end_time - start_time) * 1000
        print(
            f'\nThe function {my_function.__name__} {my_time:.2f}ms to execute.')
        return result
    return internal_function


@speed
def delayed():
    for i in range(10000):
        print(i, end=" - ")
        # sleep(1)


delayed()
