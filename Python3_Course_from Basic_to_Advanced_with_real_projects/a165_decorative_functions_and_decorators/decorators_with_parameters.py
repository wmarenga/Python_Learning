# Decorators with parameters
def decorators_factory(a=None, b=None, c=None):
    def functions_factory(func):
        print('Decorator 1')

        def nested(*args, **kwargs):
            print('Decorator parameters, ', a, b, c)
            print('Nested')
            res = func(*args, **kwargs)
            return res
        return nested
    return functions_factory


@decorators_factory(1, 2, 3)
def my_sum(x, y):
    return x + y


decorator = decorators_factory()
multiply = decorator(lambda x, y: x * y)

ten_plus_five = my_sum(10, 5)
ten_times_five = multiply(10, 5)
print(ten_plus_five)
print(ten_times_five)
