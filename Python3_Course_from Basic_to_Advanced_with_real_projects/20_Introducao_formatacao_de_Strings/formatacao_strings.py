nome = 'Luiz'
idade = 32
altura = 1.80
eh_maior = idade > 18
peso = 80
# IMC = peso / (altura * altura)
imc = peso / (altura ** 2)

# Utilizando f-strings:
print(f'O {nome} tem {idade} anos de idade e seu IMC é {imc:.2f}.')

# Utilizando o format():
print('{} tem {} anos de idade e seu IMC é {:.2f}.'.format(nome, idade, imc))

# Obs: Temos que seguir a mesma ordem dos parênteses.

# Se quisermos alterar a ordem, temos que inserir números sequenciais
# dentro dos parênteses (indexados).
print('{0} tem {2:.2f} anos de idade e seu IMC é {1}.'.format(nome, idade, imc))

# Se quisermos alterar a ordem, temos que inserir parâmetros nomeados
# dentro dos parênteses.
print('{i} tem {n} anos de idade e seu IMC é {im:.2f}.'.format(
    n=nome, i=idade, im=imc))
