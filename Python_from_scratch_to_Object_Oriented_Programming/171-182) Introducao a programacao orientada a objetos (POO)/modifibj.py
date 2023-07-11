# Modifying Object Properties 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def firstFunc(self):
        print(f"Hi, my name is: {self.name}")

obj1 = Person("Terry", 36)

# obj1.age = 50
# obj1.name = "Jack"

# print(obj1.age)
# print(obj1.name)

#del obj1.age
#print(obj1.age)
obj1.firstFunc()