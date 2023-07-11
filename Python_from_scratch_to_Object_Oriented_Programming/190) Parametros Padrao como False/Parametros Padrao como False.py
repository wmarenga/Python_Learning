# Parametros Padrao como False

class Pessoa:
    # Quando determinamos um parametro como False, estamos determinando para o nosso interpretador ignorar o mesmo (estruturas opcionais para o codigo)
    def __init__(self, nome, idade, sexo=False, altura=False):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura


pessoa1 = Pessoa('Fernando', 33)

print(pessoa1.nome)

pessoa1.sexo = 'M'

print(pessoa1.sexo)
