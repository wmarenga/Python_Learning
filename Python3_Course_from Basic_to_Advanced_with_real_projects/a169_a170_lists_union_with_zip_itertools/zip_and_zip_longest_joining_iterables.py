"""
Zip => Joining iterables
Zip_longest => Itertools
"""
from itertools import zip_longest, count

# index = range(100, 1000, 10)  # 100, 110, 120
index = count()
cities = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Other']
states = ['SP', 'MG', 'BA']

# Will join by the shortest list:
cities_states = zip(index, states, cities)
# Generate an infinite loop
# cities_states = zip_longest(index, states, cities, fillvalue='state')

# It is an iterator (one number at a time):
for index, state, city in cities_states:
    print(index, state, city)

print(list(zip_longest(cities, states, fillvalue="No name")))
