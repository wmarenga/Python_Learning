"""
nome = str(input('Qual é o seu nome? ')).strip().title()
if nome == 'Wellington':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal {}!'.format(nome))
print('Bom dia {}!'.format(nome))

# Condição Composta:

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('A sua média foi boa! Parabéns!')
else:
    print('A sua média foi ruim! Estude Mais!')

# Condição Simples:

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
print('Parabéns!' if m >= 6 else 'Estude!')

"""
