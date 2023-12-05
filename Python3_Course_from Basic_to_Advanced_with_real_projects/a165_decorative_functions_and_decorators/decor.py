'''
# Functions as variables:
def say_hi():
    print('Hello!')


# The variable is equal to the function:
variable = say_hi
print(type(variable))  # function
variable()  # Hi
'''

'''
# A function within another:
def master():
    # Internal function
    def slave():
        print('Hi')
    #Function to be performed
    return slave

# Variable receives function
variable = master()
# Performs the internal master function
variable()
'''

'''
# Function as a parameter:
def master(my_function):
    # Internal function
    def slave():
        # executes the sent function
        my_function()
    # Returns the internal function without executing
    return slave

# Any function
def say_hi():
    print('Hello!')

# Variable as function
variable = master(say_hi)

# Executes the variable/function
variable()
'''

'''
# Receives a function
def master(my_function):
    # Create an internal function
    def slave():
        # Decorate
        print('I'm decorated.')
        # Execute the sent function
        my_function()
    # Returns the internal function without executing
    return slave

# Any function
def say_hi():
    print('Hello!')

# Decorating
say_hi = master(say_hi)
say_hi()
'''

'''
# Decorator function
def master(my_funtion):
    def slave():
        print('I'm decorated.')
        my_funtion()
    return slave

# Sintax sugar of Decorator
@master
def say_hi():
    print('Hello!')

say_hi()
'''

'''
# Decorating with parameters
def master(my_funtion):
    def slave(*args, **kwargs):
        print('I'm decorated.')
        my_funtion(*args, **kwargs)
    return slave

@master
def say_hi(msg):
    print(msg)


say_hi('Hi, I am Wellington.')
'''




from time import time
from time import sleep
def speed(my_funtion):
    """
    Decorator function: Checks the time a function takes to execute.
    """
    def involves(*args, **kwargs):
        """ Function that wraps around and executes another function """
        # Start time
        start = time()
        # Executes the function
        result = my_funtion(*args, **kwargs)
        # Final time
        end = time()
        # Time result in ms
        my_time = (end - start) * 1000
        # Shows the time
        print(f'\nThe function took {my_time:.2f}ms to be executed.')
        # Returns the original function executed
        return result
    # Returns the function that involves
    return involves


@speed
def delay(qtt):
    """ Decorated function """
    for i in range(qtt):
        print(i, end='')


# Executa a função decorada
delay(10000)
