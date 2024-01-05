"""
repetitions with while

Performs an action while a condition is true
Infinite loop -> When a code has no end
"""
counter = 0

while counter <= 100:
    counter += 1

    if counter == 6:
        print("I won't show the 6.")
        continue

    if counter >= 10 and counter <= 27:
        print(f"I won't show the {counter}")
        continue

    print(counter)

    if counter == 40:
        break


print("It's over!")
