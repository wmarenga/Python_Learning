"""
While / Else:
counters
accumulators

"""
counter = 1
accumulator = 1

while counter <= 100:
    print(f'counter={counter} e accumulator={accumulator}')

    accumulator += counter
    counter += 1
else:  # The else will only be executed when while becomes False.
    while counter > 0:
        accumulator -= counter
        counter -= 1
        print(f'counter={counter} e accumulator={accumulator}')
print('This will be executed.')
