class Eletronico:
    def __init__(self, nome):
        # protegido para não aparecer quando instanciar a classe.
        self._nome = nome
        self._ligado = False  # Desligado

    def ligar(self):
        if self._ligado:  # se self._ligado = True, sai e não faz nada.
            return
        self._ligado = True  # se não estiver ligado. ligar

    def desligar(self):
        if not self._ligado:  # se self._ligado = False, sai e não faz nada.
            return
        self._ligado = False  # se estiver ligado. desligar
