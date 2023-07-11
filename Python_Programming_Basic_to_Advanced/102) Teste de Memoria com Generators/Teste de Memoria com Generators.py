"""
Teste de Memoria com Generators (teste de eficiência):

# Sequência de Fibonacci => 1, 1, 2, 3, 5, 8, 13, ...,  (número anti-anterior + número anterior)

def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums
    
# Teste 1 Função usando Lista (490 Mb)

for n in fib_lista(100000):
    print(n)
    
# Função usando geradores (mais eficiente)

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1

# Teste 2 Geradores (4.44 Mb):
for n in fib_gen(100000):
    print(n)
"""