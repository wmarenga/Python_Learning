# De Igualdade
print(5 == 6)
print(12 == 12)

# De Diferenca
print(7 != 3)

# Compostas
# Ambas tem que ser True
print(7 != 3 and 2 > 3)

# Membro is
num1 = 4
num2 = 9
num3 = 9

print(num1 == num2)
print(num1 is num2)
# O correto e usar ==
print(num2 == 9)
print(num2 is num3)

# Membro in
lista = [1, 2, 3, 'Ana', 'Maria']
print(2 in lista)
print('Maria' in lista)
print('Carlos' in lista)

# Negacao Logica
lista = [1, 2, 3, 'Ana', 'Maria']
print('Maria' not in lista)
print(4 not in lista)

# Comparativo
idade = 3
print(idade > 4)

# Maior ou Igual que
num1 = 5
print(num1 >= 7)

# Entre variaveis
x = 2
z = 5
print(x > z)
print(x >= z)

# Menor ou Igual a que
y = 7
z = 5
print(z <= y)

# Compostas Entre Operadores Logicos
x = 2
y = 7
print(x is 2 and y != x)

# De Identidade
aluguel = 250
energia = 250
agua = 65

print(aluguel is energia)
# O valor de aluguel e o mesmo valor de energia?

print(aluguel is agua)
# O valor de aluguel e o mesmo valor de agua?
