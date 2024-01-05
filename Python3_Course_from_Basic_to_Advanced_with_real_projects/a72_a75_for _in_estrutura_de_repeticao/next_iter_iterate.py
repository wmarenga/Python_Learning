"""
Iterable -> str, range, etc (__iter__)
Iterator -> who knows how to deliver one value at a time
next -> give me the next value
iter -> give me your iterator
"""
# * Example:
text = iter("Luiz")  # .__iter___()

print(next(text))  # .__next__()
print(next(text))  # .__next__()
print(next(text))  # .__next__()
print(next(text))  # .__next__()
print(next(text))  # Error: StopIteration

# for letter in text
text = 'Luiz'  # iterable

# iterator = iter(texto)  # iterator

# while True:
#     try:
#         letter = next(iterator)
#         print(letter)
#     except StopIteration:
#         break

for letter in text:
    print(letter)
