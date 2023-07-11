"""
Classes (POO):

Em POO, Classes nada mais são do que modelos dos objetos do mudo real
sendo representados computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das
lâmpadas da sua casa.

# Representação
idade = 32
preco = 2340.45
nome = 'Felicity Jones'

# Poderíamos criar uma Classe representado um lâmpada.

class Lampada:
    pass


lamp = Lampada()
print(type(lamp))

Classes podem conter:

- Atributos (variáveis) => Representam as características do objeto.
Ou seja, pelos atributos conseguimos representar computacionalmente
os estados de um objeto. No caso da lâmpada, possivelmente iríamos
querer saber se a lâmpada é 110 ou 220 volts, se ela é branca,
amarela, vermelha ou outra cor, qual é a luminosidade dela e etc.

- Métodos (funções) => Representam os comportamentos do objeto. Ou seja,
as ações que este objeto podem realizar no seu sistema. No caso da lâmpada,
por exemplo, um comportamento comum que muito provavelmente iríamos querer
representar no nosso sistema é o de ligar e desligar a mesma.

Em Python, para definirmos uma classe utilizamos a palavra reservada class.

Obs: Utilizamos a palavra (pass), quando temos um bloco de código que ainda
não está implementado. Usando (pass), determinamos que nada será executado.

Obs: Quando nomeamos nossas classes em Python, utilizamos por convensão o
nome com inicial em maiúsculo. Se o nome for composto, utiliza-se as iniciais
de ambas as palavras em maiúsculo, todas juntas (CamelCase por convensão).

Exemplo:

class ContaCorrente:
    pass

Dica Geek: Em computação não utilizamos: Acentuação, caracteres especiais,
espaços ou similares para nomes de classes, atributos, métodos, arquivos,
diretórios e etc.

Exemplo:
maçã = giyugiug

Em Java, temos que criar um arquivo como o mesmo nome da classe:
Lampada.java e dentro a classe Lampada.

Em Python, podemos criar um arquivo com qualquer nome e inserir várias
classes dentro deste arquivo.

class Lampada:
    pass
class ContaCorrente:
    pass
class Produto:
    pass
class Usuario:
    pass

valor = int('42')  # cast (convertendo a string para o tipo inteiro)
help(int)

As classes internas do Python, são todas em minúscula e sem os dois ponto (:).
class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer

Obs: Quando estamos planejando um software e definimos quais classes teremos
que ter no sistema, chamamos estes objetos que seão mapeados para classes de
entidades.
"""
