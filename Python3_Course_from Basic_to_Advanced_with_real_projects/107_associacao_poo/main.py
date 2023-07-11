from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

# Instanciando uma variável escritor para as classes.
escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

# Criamos uma variável para instanciar MaquinaDeEscrever()
escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()
