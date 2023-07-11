"""
O que e Programação Orientada a Objetos? (POO)

- POO é um paradigma de programação que utiliza mapeamento de objetos
do mundo real para modelos computacionais.

- Paradigma de programação é a forma/ metodologia utilizada para pensar/
desenvolver sistemas.

Paradigmas da Programação (mais utilizados):
- Programação Estruturada;
- Programação Orientada a Objeto;
- Programação Funcional.

Uma função dentro de uma classe é chamada de método.

Principais elementos da Orientação a Objetos:

- Classe => Modelo do objeto do mundo real sendo representado computacionalmente.
- Atributo => Características do objeto.
- Método => COmportamento do objeto (funções).
- Construtor => Método especial utilizado para criar os objetos.
- Objeto => Instância da classe.

Quando escrevemos as nossas classes, nós estaremos definindo o nosso próprio
tipo de dados (nosso modelo).

numero = 10
print(numero)
print(type(numero))

nome = 'Geek'
print(nome)
print(type(nome))


class Produto:
    pass


produto4 = Produto()
# produto4 => É um objeto da classe Produto
# Produto() => É o método contrutor padrão da classe Produto
print(produto4)
print(type(produto4))  # <class '__main__.Produto'>
"""
