paiseseuro = ['Alemanha', 'Autria', 'Belgica', 'Bulgaria',
              'Chequia', 'Chipre', 'Croacia', 'Dinamarca', 'Eslovaquia',
              'Eslovenia', 'Espanha', 'Estonia', 'Finlandia', 'França',
              'Grecia', 'Hungria', 'Irlanda', 'Italia', 'Letonia', 'Lituania',
              'Luxemburgo', 'Malta', 'Paises Baixos', 'Polonia', 'Portugal',
              'Romenia', 'Suecia']
ordem = 1
pergunta = []
euro = []
while ordem < 3:
    pergunta.append(input(f'Digite o {ordem}º país que acredita que compõem a União Europeia: '))
    if pergunta[0] in paiseseuro:
        euro.append(pergunta)
    ordem += 1
print(pergunta)
print(euro)