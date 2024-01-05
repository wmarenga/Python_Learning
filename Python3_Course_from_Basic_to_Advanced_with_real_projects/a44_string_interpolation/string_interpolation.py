"""
Basic string interpolation
s - string
d and i - int
f - float
x and X - Hexadecimal (ABCDEF0123456789)
"""
name = 'Luiz'
price = 1000.95897643
variable = '%s, the price is €%.2f' % (name, price)
print(variable)
print('The hexadecimal of %d is %08X' % (1500, 1500))
# ! 08X => 8 decimal places in total with zeros filled in for missing places.
