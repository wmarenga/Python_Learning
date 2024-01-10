# Understanding self in Python classes:

# Class - Mold (usually no data)
# Instance of the class (object) - Has the data
# A class can generate multiple instances.
# In the class, self is the instance itself.
# The self is just a convention.

class Car:
    def __init__(self, name):
        self.name = name
    # def __init__(abc, name):
    #     abc.name = name

    def speed_up(self):
        print(f'{self.name} is accelerating...')
    # def speed_up(efg):
    #     print(f'{efg.name} is accelerating...')


fusca = Car('Fusca')
fusca.speed_up()
Car.speed_up(fusca)
# print(fusca.name)
# fusca.speed_up()

celta = Car(name='Celta')
celta.speed_up()
Car.speed_up(celta)
# print(celta.name)
