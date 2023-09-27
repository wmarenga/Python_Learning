# ShalloCopy and DeepCopy:
import copy


d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

d2 = d1  # shallowcopy
d2 = d1.copy()  # deepcopy
# By changing one dictionary, the other will not be affected.
# Using import copy, we can define exactly which copy we want
# (deepcopy or shallowcopy).
d2 = copy.deepcopy(d1)

# !Note: For immutable data, .copy() works perfectly, but when we have
# !mutable data within the dictionary (e.g. list), a shallowcopy is made.
d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)
