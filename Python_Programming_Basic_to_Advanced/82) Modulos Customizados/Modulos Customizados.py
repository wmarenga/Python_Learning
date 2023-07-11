"""
Módulos Customizados:

Como módulos Python nada mais são do que arquivos Python, então TODOS
os arquivos que criamosneste curso são módulos Python pronto para
serem utilizados.

# Importando todo o módulo (temos acesso a TODOS os elementos do módulo)
import funcoes_com_parametros as fcp

# Importanto uma funcao especifica do nosso módulo
from funcoes_com_parametros import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Estamos acessando e imprimindo uma variavel contida no módulo
print(fcp.lista)

print(fcp.tupla)

print(fcp.soma_impares(fcp.lista))
"""

from Map import cidades, conv_cels_fah

print(list(map(conv_cels_fah, cidades)))
