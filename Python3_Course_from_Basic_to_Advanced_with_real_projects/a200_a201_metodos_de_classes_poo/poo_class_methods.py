"""
When to use an instance or class method?

- This method is related to the class (mold in general)
or the instance, that is, specific to each object. Each
object will have a different value.
"""


class People:
    # class attribute (current_year)
    current_year = 2019

    # Instance Methods
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance Methods
    def get_birth_year(self):
        print(self.current_year - self.age)

    # By creating a class method we will have access
    # to a variable that is an attribute of the class (current_year).
    @classmethod
    def get_age(cls, name, birth_year):
        age = cls.current_year - birth_year
        return cls(name, age)


# p1 = People.get_age('Luiz', 1987)
p1 = People('Luiz', 32)
print(p1)
print(p1.name, p1.age)
print(p1.age)
p1.get_birth_year()
