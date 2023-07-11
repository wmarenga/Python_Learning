# Desafio 24:
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não
# com o nome "santo".

cidade = str(input('Digite o nome da cidade em que nasceu: ')).strip()
if (cidade[:5].lower() == 'santo') is True:
    print('A cidade em que você nasceu começa com {}!'.format(
        cidade[:5].capitalize()))
else:
    print('A cidade em que você nasceu não começa com Santo!')
