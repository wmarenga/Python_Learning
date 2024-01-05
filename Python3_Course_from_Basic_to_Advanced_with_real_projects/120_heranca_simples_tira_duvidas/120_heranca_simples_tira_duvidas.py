"""
Animal --> respirar/ Animal não herda uivar
    Lobo(Animal)  --> herda respirar de Animal
                  --> uivar
    Cachorro(Lobo)  --> herda respirar de Lobo que herdou de Animal
                    --> herda também uivar de Lobo
                    --> latir (somente Cachorro tem o método latir, ninguém herdou)

A herança virá da classe pai para a(s) classe(s) filha(s).
# As classes pai afetam as classes filhas, contudo as classes filhas não afetam as classes pais.

*******************************************
Biblioteca
    Interface(Biblioteca)
        metodo_da_interface

Obs.: É possível a classe pai chamar um método da classe filha, porém não é muito comum e também muito complexo.
"""
from classes.interface import Interface
i1 = Interface()
i1.metodo_da_interface()
