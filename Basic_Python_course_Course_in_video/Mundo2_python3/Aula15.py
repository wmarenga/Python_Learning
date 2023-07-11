"""
cont = 1
while cont <= 10:
    # Deixar um espaço com seta e todo na mesma linha "end=".
    print(cont, '->', end='')
    cont += 1
print('Acabou')

# Digita 3 vezes o número e para.
n = cont = 0
while cont < 3:
    n = int(input('Digite um número: '))
    cont += 1

# Enquanto não digitar o 999 pede para digitar.
n = 0
while n != 999:
    n = int(input('Digite um número: '))

# Realiza a soma porém acrescentando o 999.
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
print('A soma vale {}'.format(s))

n = s = 0
while True:
    n = int(input('Digite um número: '))
    # Usamos o comando "break" para interromper o loop sem contabilizar a última digitação.
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))

# A partir da versão 3.6 do Python podemos as FString.
# Utilizamos o "f" antes da aspas e inserimos a variável dentro dos colchetes.
print(f'A soma vale {s}')

nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.') # Python 3.6 ou superior
print('O {} tem {} anos.'.format(nome, idade)) # Python 3
print('O %s tem %d anos.' % (nome, idade)) # Python 2

nome = 'José'
idade = 33
salário = 987.3
print(f'O {nome} tem {idade} anos e ganha R$ {salário:.2f}')
# Nome com 20 espaços
print(f'O {nome:20} tem {idade} anos e ganha R$ {salário:.2f}')
# Nome Centralizado com traços
print(f'O {nome:-^20} tem {idade} anos e ganha R$ {salário:.2f}')
# Alinhado a direita
print(f'O {nome:->20} tem {idade} anos e ganha R$ {salário:.2f}')
# Alinhado a esquerda
print(f'O {nome:-<20} tem {idade} anos e ganha R$ {salário:.2f}')

"""
