# Concatenando diferentes tipos de dados em uma string

nome = 'Ana Clara'
idade = 12

print(f'{nome} tem {idade} anos.')

aviso = f'Atencao, geradores entrarao em manutencao as: {idade} horas!'

aviso = 'Atencao, geradores entrarao em manutencao as: ' + str(idade) + ' horas!'

print(aviso)
