# Desafio 49:
# Refaça o desafio 9, mostrando a TABUADA de um número que
# o usuário escolher, só que agora utilizando um LAÇO FOR.

num = int(input('Digite um número para saber a tabuada dele: '))
for c in range(1, 11):
    print('{} X {:>2} = {}'.format(num, c, c * num))
