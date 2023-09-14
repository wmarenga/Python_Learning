"""
Manipulating str:

Docs:
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html

- String indexes;
- String slicing [start:end:step];
Note: it starts at the informed position, but ends one position earlier.
- Built-in functions len, abs, type, print, etc...
These functions can be used directly on each type.

"""
# Positives
# index[012345678]
text = 'Python s2'
print(text[2])  # t
print(text[2])  # 2
print(text[6])  # empty spaces

# Negatives
# index[987654321]
text2 = 'Python_s3'

url = 'www.google.com.br/'
print(url[:-1])  # Displays without the last character

# Slicing str
# Positivos
new_string = text2[2:6]  # will not be included the 6.
print(new_string)
new_string2 = text2[:6]  # start up to 5 position.
print(new_string2)
new_string3 = text2[7:]  # starts in position 7 until the end.
print(new_string3)

# Negatives
# 'Python s3'  [-9,-8,-7,-6,-5,-4,-3,-2,-1]
new_string4 = text2[-1]  # Last position.
print(new_string4)
new_string5 = text2[-9]  # first position.
print(new_string5)
new_string6 = text2[-9:-1]  # first position to the penultimate position.
print(new_string6)

# Skipping characters [start:end:step]
new_string7 = text2[0:7:2]
print(new_string7)
new_string7 = text2[0::3]  # From the beginning to the end, 3 by 3.
print(new_string7)
