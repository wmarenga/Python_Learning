"""
Basic string formatting:
s - string
d - int
f - float
.<number of digits>f
x or X - Hexadecimal
(Character)(><^)(quantity)
> -> left
< -> right
^ -> center
= -> Forces the number to appear after the signal.
Signal - + (display - and + signal) or - (display only negative signal)
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
!r -> __repr__ (reper method)
!s -> __str__ (string method)
!a -> __asc__ (asc method)

! Converting Hexadecimal to Decimal
# First, initialize the string   
numero_hex = '000005DC'

# then, Print the original string   
print ("The Hexadecimal string is: " + str(numero_hex))

# now, use the int() function to convert the hexadecimal string to decimal string  
convertion = int(numero_hex, 16)

# At last, print result
print ("The converted hexadecimal string into decimal string is: " + str(convertion))

"""
variable = 'ABC'
print(f'{variable}')
print(f'{variable:*>10}')
print(f'{variable:-<10}.')
print(f'{variable: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal of 1500 is {1500:08X}')
print(f'{variable!r}')
