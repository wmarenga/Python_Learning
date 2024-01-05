# Examplo 1 (shortcut)
name = input('What is your name? ')
print(name or "You didn't type anything!")

# Examplo 2
a = 0
b = None
c = False
d: list = []
e: dict = {}
f = 22
g = 'Wellington'

variable = a or b or c or d or e or f or g
# Displays the first True => 22
print(variable)

# The manual way (more laborious)
if a:
    variable = a
elif b:
    variable = b
elif c:
    variable = c
elif d:
    variable = d
elif e:
    variable = e
elif f:
    variable = f
else:
    variable = g
