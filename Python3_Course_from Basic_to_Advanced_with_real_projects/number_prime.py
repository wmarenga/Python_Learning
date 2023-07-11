def is_prime(num):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return num


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
