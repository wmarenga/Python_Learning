# Aplicacao de Orientacao a Objetos

from base import BaseDeDados

clientes = BaseDeDados()

clientes.inserir('Ana', 991358899)
clientes.inserir('Fernando', 981357295)
clientes.inserir('Maria', 999891415)

clientes.listar()

clientes.apagar('Ana')

clientes.listar()
