"""
Assignment Operators:
= += -= *= /= //= **= %=
"""
counter = 10

###

counter /= 5
print(counter)

# Note: We can use with string too.
counter = '1'
counter += '2'
print(counter)  # Output '12' (concatenation)

counter = 10
counter += '2'
print(counter)  # Output '2222222222' (repetition)
