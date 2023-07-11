# Desafio 62:
# Melhore o DESAFIO 61, perguntado para o usuário se ele
# quer mostrar mais alguns termos. O programa encerra
# quando ele disser que quer mostrar OS TERMOS.

print('='*10)
nome = 'GERADOR DE PA'
print('{:^30}'.format(nome))
print('='*10)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos quer adicionar: '))
print('Progressão finlizada com {} termos mostrados.'.format(total))
