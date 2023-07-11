# creating a greeting function and execute it on the object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def firstfunc(self):
        print("Hi, my name is: " + self.name)

obj1 = Person("Terry", 40)
obj1.firstfunc()
