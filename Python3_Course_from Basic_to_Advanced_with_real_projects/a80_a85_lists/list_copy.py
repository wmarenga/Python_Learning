"""
Care for mutable data
=> copied the value (immutable)
=> points to the same value in memory (mutable)
"""
list_a = ['Luiz', 'Maria', 1, True, 1.2]
list_b = list_a.copy()

list_a[0] = 'Anything'
print(list_a)
print(list_b)
