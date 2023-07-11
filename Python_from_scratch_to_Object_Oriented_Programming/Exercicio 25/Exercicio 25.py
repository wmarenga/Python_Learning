''' Crie um programa que realiza a Progressao Aritmetica de 20 elementos
com primeiro termo e razzao definidos pelo usuario.'''

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
n = int(input('Quantos elementos quer exibir? '))

ultimo = termo + (n - 1) * razao

for i in range(termo, ultimo + 1, razao):
    print(i)
