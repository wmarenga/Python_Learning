# Methods in Python class instances
# Hard coded - It is something that was written directly in the code
# The __init__ method always returns None.
# A method is a function within a class.

class car:
    def __init__(self, name):
        # self.name = 'Fusca' # Hard coded
        self.name = name

    def speed_up(self):
        print(f'{self.name} is accelerating...')


string = 'Luiz'
print(string.upper())

fusca = car('Fusca')
print(fusca.name)
fusca.speed_up()

celta = car(name='Celta')
print(celta.name)
celta.speed_up()
