# Exercise - Postponing execution of functions:

def my_sum(x, y):
    return x + y


def multiplication(x, y):
    return x * y


def function_creation(my_function, y):
    def postponing_function(x):
        return my_function(x, y)
    return postponing_function


sum_with_five = function_creation(my_sum, 5)
multiplication_by_ten = function_creation(multiplication, 10)

print(sum_with_five(10))
print(multiplication_by_ten(10))
