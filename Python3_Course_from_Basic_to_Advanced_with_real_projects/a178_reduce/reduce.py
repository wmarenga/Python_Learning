from data import products, people, my_list
from functools import reduce

#! Example accumulating all values from my_list
accumulate = 0
for item in my_list:
    accumulate += item

print(accumulate)

#! Example with lambda
# Reduce(accumulated function(ac), item in my_list(i): i + ac, my_list, start)
sum_list = reduce(lambda ac, i: i + ac, my_list, 0)
print(sum_list)

#! Example with dictionary
sum_price = reduce(lambda ac, p: round(p['price'] + ac, 2), products, 0)
print(sum_price)
print(round(sum_price / len(products), 2))  # average prices

#! Example with ages

sum_ages = reduce(lambda ac, p: ac + p['age'], people, 0)
print(sum_ages)
print(sum_ages / len(people))  # average ages
