"""
Just like map, the filter function does not return
a list but rather an iterator of type map. To
resolve this, we must cast it to make it a list.

#! Example

from data import products, people, my_list

new_list = filter(lambda x: x > 5, my_list)
print(new_list)

#! Example with list comprehension

new_list2 = [x for x in my_list if x > 5]
print(list(new_list2))

#! Example

new_list3 = filter(lambda p: p['price'] > 20, products)
for product in new_list3:
    print(product)

#! Example more complex


def filtering(product):
    if product['price'] > 50:
        product['is_expensive'] = True
    return True


new_list4 = filter(filtering, products)

for product in new_list4:
    print(product)

"""

from data import products, people, my_list

#! Example filter on people (of legal age)


def filtering(people):
    if people['age'] >= 18:
        return True


new_list5 = filter(filtering, people)

for product in new_list5:
    print(product)
