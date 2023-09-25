"""
* Exercise

Create functions that double, triple and quadruple
the number received as a parameter.
"""


# def multiplier(multiplier_factor):
#     def multiply(num):
#         result = multiplier_factor * num
#         return result
#     return multiply


# double = multiplier(2)
# triple = multiplier(3)
# quadruple = multiplier(4)

# print(double(2))
# print(triple(2))
# print(quadruple(2))

# *Exercise (multiplication table):


# def multiplier(multiplier_factor):
#     def multiply(num):
#         result = multiplier_factor * num
#         return result
#     return multiply


# for n1 in range(1, 11):
#     for n2 in range(1, 11):
#         mult = multiplier(n1)
#         print(f"{n1} X {n2} = {mult(n2)}")
#         if n2 == 10:
#             print(13 * '*')


# *Exercise (multiplication table using dictionary):

def multiplier(multiplier_factor):
    def multiply(num):
        result = multiplier_factor * num
        return result
    return multiply


dict_table = dict()


for n1 in range(1, 11):
    for n2 in range(1, 11):
        mult = multiplier(n1)
        dict_table[f"{n1} X {n2} ="] = mult(n2)

for i, v in enumerate(dict_table):
    print(f"{v} {i}")
