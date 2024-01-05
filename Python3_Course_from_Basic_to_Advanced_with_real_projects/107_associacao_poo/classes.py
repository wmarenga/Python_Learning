class Escritor:
    def __init__(self, nome):
        # Tem a amesma função do setter (atribuindo nome para self.nome)
        self.__nome = nome
        self.__ferramenta = None

    # Criamos este getter para conseguir acessar o atributo privado
    # do __init__.
    @property
    def nome(self):
        return self.__nome

    # Criando getter para ferramento (buscar informações) = privadas
    @property
    def ferramenta(self):
        return self.__ferramenta

    # Criando setter para ferramento (atribuir informações) = privadas
    @ferramenta.setter
    def ferramenta(self, ferramenta_alterada):
        self.__ferramenta = ferramenta_alterada


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    # Criamos este getter para conseguir acessar o atributo privado
    # do __init__.
    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')


class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está escrevendo...')
