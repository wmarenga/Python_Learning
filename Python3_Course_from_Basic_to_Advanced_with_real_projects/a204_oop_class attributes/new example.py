# Class attributes


class People:
    current_year = 2022  # Class attributes

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.current_year = 100 (It will be primarily searched for in __init__)

    def get_birth_date(self):
        return People.current_year - self.age


p1 = People('João', 35)
p2 = People('Helena', 12)

print(People.current_year)
# People.current_year = 1 (We are changing the class attribute.)

print(p1.get_birth_date())
print(p2.get_birth_date())
