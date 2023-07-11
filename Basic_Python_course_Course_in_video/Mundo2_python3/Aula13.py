"""
# Contagem progressiva:
for c in range(1, 6):  # O Python conta de 1 a 5, pois desconsidera o 6.
    print(c)
print('FIM!')

# Contagem regressiva:
for c in range(6, 0, -1):
    print(c)
print('FIM!')

# Contagem progressiva de 2 em 2:
for c in range(0, 7, 2):
    print(c)
print('FIM!')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM!')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM!')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n  # (s = s + n)
print('O somatório de todos os valores foi {}'.format(s))
"""
