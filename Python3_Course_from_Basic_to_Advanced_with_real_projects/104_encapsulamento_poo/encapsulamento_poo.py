"""
Encapsulamento - POO:

Tipos de encapsulamento:

São utilizados os encapsulamentos afim de protegem a sua aplicação.

Métodos e atributos:

- publico (podem ser acessados dentro e fora da classe);
- protected (podem ser acessados somente dentro da classe com
suas respectivas filhas da classe);
- private (só está disponível dentro da classe).

Convensões:
_  privado/ protected (um underline)     => Recomendá-se não acessar este os
                        atributos (proteção fraca - ainda acessível).
__ privado  (dois underlines)  => proteção forte - não acessível
Conseguimos acessar dessa maneira: (_NOMECLASSE__nomeatributo)
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')
# Alterando o atributo principal (clientes para Uma outra coisa),
# todo o programa será quebrado, pois todos os métodos da classe foram definidos como 'clientes'.
# bd.__dados = 'Uma outra coisa'
# bd.apaga_cliente(2)
# bd.lista_clientes()
bd.__dados = 'Um outro valor'  # conseguimos até alterar valores.
# bd.lista_clientes()
# print(bd.__dados)
# print(bd._BaseDeDados__dados)  # mostrando dados protegidos

# Liberando acesso aos valores do atributo


class BaseDeDados2:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados


bd = BaseDeDados2()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
# Será levantado uma excessão pois não definimos getters e setters
# (AttributeError: can't set attribute)
bd.dados = 'Outro valor'
print(bd.dados)  # conseguimos acessar diretamente sem o underline.
