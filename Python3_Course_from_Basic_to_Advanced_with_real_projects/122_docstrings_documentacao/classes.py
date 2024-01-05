"""..."""


class MinhaClasse:
    """ Documentação normal

    Conforme qualquer outra documentação que você tenha usado anteriormente.
    """
    atributo = 1
    atributo2 = 'valor'

    def __init__(self, texto):
        """ Inicializa os dados

        :parametro texto: o texto da classe
        :type texto: str
        """
        self.texto = texto
        self.exibe_texto(texto)

    @staticmethod
    def exibe_texto(texto):
        """ Método que exibe um texto de 100 caracteres na tela

        :parametro texto: Um texto de 100 caracteres
        :type texto: str

        :return: O texto de 100 caracteres ou menos
        :rtype: str

        :raises ValueError: Se o texto tiver mais de 100 caracteres
        :raises TypeError: Se o texto não for uma string
        """
        if len(texto) > 100:
            raise ValueError('texto precisa ter 100 caracteres ou menos.')

        if not isinstance(texto, str):
            raise TypeError('texto precisa ser uma string.')

        return texto
