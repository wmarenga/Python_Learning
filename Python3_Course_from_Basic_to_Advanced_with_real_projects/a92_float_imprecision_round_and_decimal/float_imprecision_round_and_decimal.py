"""
Floating point inaccuracy
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal

number_1 = decimal.Decimal('0.1')
number_2 = decimal.Decimal('0.7')
number_3 = number_1 + number_2
print(number_3)
print(f'{number_3:.2f}')
print(round(number_3, 3))

# ! If we use without ' ', we are allowing to display the number precisely.
# number_1 = decimal.Decimal(0.1)
# number_2 = decimal.Decimal(0.7)
# number_3 = number_1 + number_2  # Output: 0.7999999999999999611421941381
