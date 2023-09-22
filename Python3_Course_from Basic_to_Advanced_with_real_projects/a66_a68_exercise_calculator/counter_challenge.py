"""
Counter challenge:

for/ while
0 10
1  9
2  8
3  7
4  6
5  5
6  4
7  3
8  2
"""
# With while

c1 = 0
c2 = 10
while True:
    if c1 <= 10:
        print(f'Counter 1 = {c1}')
        c1 += 1
    elif c2 >= 2:
        print(f'Counter 2 = {c2}')
        c2 -= 1

# With for

# for c1, c2 in enumerate(range(10, 0, -1), start=1):
#     print(c1, c2)
