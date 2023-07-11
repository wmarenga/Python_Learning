'''
Estruturas de Repeticao:

- Muitas vezes estruturas de codigos tem que ser repetidas;
- Em muitos casos, estas repeticoes sao definidas dinamicamente (input do usuario). 

Exemplo:

- Entre o salario dos 5 funcionarios:
    * Func1 = float(input())
    * Func2 = float(input())
    * Func3 = float(input())
    * Func4 = float(input())
    * Func5 = float(input())
- Entre a quantidade de funcioanrios, e em seguida, o salario de cada um:
    * ?

while (executa o comando enquanto a condicao for verdadeira):
    
count = 1
while count <= 5:
    print(count)
    count += 1

FOR (usamos o FOR para executar um numero de vezes):

for n in range(10, 0, -2):
    print(n)

** range (valor inicial, valor final, incremento)
   range(0, 10, 1) - vai de 0 a 9 de 1 em 1. 
   O incremento e opcional e podera ser negativo.

for n in range(10, 0, -2):
    print(n)

Output: 10, 8, 6, 4, 2

Interrupcoes:

** Interrupcao de um laco (sai fora do laco):
    break
** Reiniciar um laco (incrementa o valor e volta para o inicio):
    continue

'''
