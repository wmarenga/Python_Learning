# Aplicacao de Orientacao a Objetos

class BaseDeDados:
    def __init__(self):
        # Criacao de um dicionario vazio
        self.base = {}

    def inserir(self, nome,  fone):
        if 'clientes' not in self.base:
            # Se nao existir e chave 'clientes' no dicionario em self.base, criar os dados e a chave 'clientes'
            self.base['clientes'] = {nome: fone}
        else:
            # Caso contrario atualizar a chave existente com novos dados dentro
            self.base['clientes'].update({nome: fone})

    def listar(self):
        ''' Poderiamos inserir qualquer valor no lugar de nome e fone no FOR
        (desempacotamento do dicionario) - variaveis temporarias'''
        for n, f in self.base['clientes'].items():
            print(n, f)

    def apagar(self, nome):
        del self.base['clientes'][nome]
