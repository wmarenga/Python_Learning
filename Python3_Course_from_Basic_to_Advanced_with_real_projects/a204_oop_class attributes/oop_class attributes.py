"""
Class attributes - OOP:

class A:
    vc = 123


a1 = A()
a2 = A()

A.you = 321  # Change the class variable for all instances.

# We are not changing the class variable and just creating
# a direct attribute in the instance (a1 or a2)

a1.you = 444  # We only change instance a1
print(a1.you)  # Instantiating as a1
print(a2.you)  # Instantiating as a2
print(A.you)   # straight from the class

print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)
"""


class A:
    you = 123

    def __init__(self):
        # self.you = 321
        pass


a1 = A()
a2 = A()
A.you = 'Changed'

print(a1.you)  # Instantiating as a1 (Output: 321)
print(a2.you)  # Instantiating as a2 (Output: 321)
print(A.you)  # straight from the class (Output: 123)
