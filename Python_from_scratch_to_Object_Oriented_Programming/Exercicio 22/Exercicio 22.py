''' Crie um programa que le um valor de inicio e um valor de fim, exibindo
em tela a contagem dos numeros dentro desse intervalo.'''

inicio = int(input('Digite o primeiro numero: '))
fim = int(input('Digite o ultimo numero: '))

for i in range(inicio, fim + 1):
    print(i)
