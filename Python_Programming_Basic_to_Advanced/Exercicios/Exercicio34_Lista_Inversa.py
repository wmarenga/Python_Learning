"""
Exercicio 34 - Lista Inversa:
Fazer um program que leia uma sequência de números inteiros terminado em zero, quando o 
usuário digita o zero imprime a lista em ordem inversa.
"""
lista = []
num = int(input("Digite um número inteiro terminado em zero: "))
while num % 10 == 0:
    while num != 0:
        lista.append(num)
        num = int(input("Digite um número inteiro terminado em zero: "))
        if num == 0:
            break
    print(lista.reverse())
