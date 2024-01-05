"""
Documentation:
https://docs.python.org/3/tutorial/modules.html
"""

# import sales.calc_price
# from sales import calc_price
from sales.calc_price import format_price, increase, reduction
# from sales.format import price
import sales.my_format.price as my_format

price = 49.90
price_with_increase = increase(value=price, percentage=15, my_format=True)
print(price_with_increase)
print(format_price(price_with_increase))

price_with_reduction = reduction(value=price, percentage=15, my_format=True)
print(price_with_reduction)
# print(format_price(price_with_reduction))

print(my_format.real(50))
