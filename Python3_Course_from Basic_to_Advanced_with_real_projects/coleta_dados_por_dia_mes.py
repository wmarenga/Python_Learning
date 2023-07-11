"""
# Array 2 X 2
temps = [[0.0 for h in range(24)] for d in range(31)]

for d in range(31):
    for h in range(24):
        temps[d][h] = float(input('Digite: '))

print(temps)
"""
# Array 3 X 3
hotel = [[[False for room in range(20)]
          for floor in range(15)] for build in range(3)]

# for build in range(3):
#    for floor in range(15):
#        for room in range(20):
#            hotel[build][floor][room] = bool(input('Digite: '))
hotel[0][0][0] = True
print(hotel)
