# Desafio 83:
# Crie um programa onde o usuário digite uma expressão qualquer que
# use parênteses. Seu aplicativo deverá analisar se a expressão passada
# está com os parênteses abertos e fechados na ordem correta.

expressão = str(input('Digite uma expressão matemática: ')).strip().upper()
análise1 = int(expressão.count('('))
análise2 = int(expressão.count(')'))
diferença = análise1 - análise2
if diferença > 0:
    print('Expressão inválida!')
    print(f'Estão faltando {abs(diferença)} parênteses para direita ).')
elif diferença < 0:
    print('Expressão inválida!')
    print(f'Estão faltando {abs(diferença)} parênteses para esquerda (.')
elif diferença == 0:
    print('A sequência está correta.')
    print(
        f'Temos {análise1} parênteses para esquerda e {análise2} parênteses para direita.')

"""
# Solução do Professor:

expressão = str(input('Digite a expressão: '))
pilha = []
for símb in expressão:
    if símb == '(':
        pilha.append('(')
        pilha.pop()
    else:
        pilha.append(')')
        break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
"""
