# Scope of the class and class methods:
# A variable created within a method of a class cannot be called
# from another method of the class.

# The unique alternative would be to assign self (self.variable)
# to the method so that it can be accessed from the entire class.

class Animal:
    # name = 'lion'

    def __init__(self, name):
        self.name = name

        variable = 'value'
        print(variable)

    def eating(self, food):
        return f'{self.name} is eating {food}.'

    def execute(self, *args, **kwargs):
        return self.eating(*args, **kwargs)


lion = Animal(name='lion')
print(lion.name)
print(lion.execute('apple'))
