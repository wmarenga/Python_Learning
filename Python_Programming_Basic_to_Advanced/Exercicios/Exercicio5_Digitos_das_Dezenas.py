"""
Exercício 3

Faça um programa em Python que recebe um número inteiro e imprime 
seu dígito das dezenas. Observe o exemplo abaixo:

Exemplo 1:

Entrada de Dados:
Digite um número inteiro: 78615

Saída de Dados:
O dígito das dezenas é 1

Exemplo 2:

Entrada de Dados:
Digite um número inteiro: 2

Saída de Dados:
O dígito das dezenas é 0

Dica: O operador "//" faz uma divisão inteira jogando fora o resto, 
ou seja, aquilo que é menor que o divisor. O operador "%" devolve 
apenas o resto da divisão inteira jogando fora o resultado, ou seja, 
tudo que é maior ou igual ao divisor.
Como enviar
Quando você estiver pronto para enviar, você pode fazer upload dos 
arquivos para cada parte da tarefa na guia "Meu envio".
"""

numero = int(input('Digite um número inteiro: '))
dezena = (numero // 10) % 10
print("O dígito das dezenas é", dezena)
