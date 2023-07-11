"""
Tipos de Dados:

Obs: Utilizamos a classe type() dentro da função print() para verificar
o tipo do dado.

str   => string (textos -> 'Assim', "Assim")
print('Assim', type('Assim'))
print('123456', type('123456'))

int   => inteiro (números sem ponto -> 123456, 10, 20, 33, -11)
print(123456, type(123456))
print(-33, type(-33))

float => real ou ponto flutuante (números com ponto -> 1.234, -12.13)
print(-12.11, type(-12.11))
print(11.44, type(11.44))

Obs: Em linguagens de programação não utilizamos a vírgula para definir
números reais.

bool  => booleano, lógico ou binário (True ou False)
print(True, type(True))
print(False, type(False))
print(10==10, type(10==10))
print(10!=10, type(10!=10))

Type Cast (casting):

str()   => print(str('meu nome'))
int()   => print(int(1234)), print(int(10.10)), print(int(-12.12)),
           print(int('10')), print(int('10') + int('10'))
Obs: Mesmo que acrescentemos o . ainda teremos um número inteiro, onde
os números após a o ponto serão ignorados.

float() => print(float(55.22)), print(float(33)), print(float(-77)),
           print(float('56.12'))
Obs: Mesmo após acrescentar um número inteiro e fazendo casting como float(),
será acrescentado o zero depois do ponto, tornando o valor real.

bool()  => print(bool([])), print(bool(0)), print(bool(''))
Obs: Alguns valores são avaliados como Falso e outros como verdadeiro.

Exemplo:
False  => print(bool([])), print(bool(0)), print(bool(''))
True   => print(bool([1])), print(bool('abc')), print(bool(10 == 10))

"""

# Exercício:
# Criar um cadastro e exiba na tela.
nome = str(input('Digite o seu nome: ')).capitalize()
idade = int(input('Digite a sua idade: '))
altura = float(input('Qual a sua altura em metros: '))
print(f'Seu nome é: {nome}. A classe do seu nome é: {type(nome)}')
print(f'Você tem {idade} anos. A classe da sua idade é: {type(idade)}')
print(
    f'A sua altura é {altura:.2f} metros. A classe da sua altura é: {type(altura)}')

# Maneira mais Avançada

# Retornando True ou False
print(
    f'Você é maior de idade: {True if idade > 18 else False}. A classe da sua comparação é: {type(True if idade > 18 else False)}')
# Retornando convertendo para: Sim ou Não
print(
    f'Você é maior de idade: {"Sim" if (True if idade > 18 else False) == True else "Não"}. A classe da sua comparação é: {True if idade > 18 else False}')

# Maneira mais Básica:

if idade > 18:
    print(
        f'Você é maior de idade: {idade > 18}. A classe da sua comparação é: {type(idade > 18)}')
else:
    print(
        f'Você é maior de idade: {idade < 18}. A classe da sua comparação é: {type(idade < 18)}')
