"""
Em Python nos podemos usar comandos simples em uma unica linha.
"""

num = [i for i in range(0,101)]
print(num)

num = [2*i for i in range(0,101)]
print(num)

soma = sum([i if i%2==0 else 0 for i in range(0,101)])
"Quando usamos comandos em linha temos que utilizar o 'else'"
print(soma)

num = [i if i%2==0 else 5 for i in range(0,101)]
print(num)

"Todos os numeros impares vou substituir por 5"

num = [i if i%2==0 else (2*i**3) for i in range(0,101)]
print(num)

"Todos os numeros impares vou substituir pela equacao (2*i**3)"

soma = 0
for i in range(0,101):
    if i%2==0:
        soma += i
print(soma)