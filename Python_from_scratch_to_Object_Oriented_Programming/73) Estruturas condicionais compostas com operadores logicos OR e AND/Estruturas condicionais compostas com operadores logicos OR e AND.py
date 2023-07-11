# Estruturas condicionais compostas com or (ou) e and (e)

veiculo1 = 'Gol'
veiculo2 = 'Corsa'
veiculo3 = 'Onibus'
cor1 = 'Branco'
cor2 = 'Vermelho'

if veiculo1 == 'Gol' or veiculo2 == 'Celta':
    print('Carro')
if veiculo1 == 'Gol' and cor1 == 'Branco':
    print(f'{veiculo1} {cor1}')
if veiculo1 == 'Onibus' and cor2 == 'Vermelho':
    print(f'{veiculo3} {cor2}')

# Condicao em or ==> apenas uma das condicoes precisa ser verdadeira.
# Condicao em and ==> as duas condicionais precisam ser verdadeiras.
