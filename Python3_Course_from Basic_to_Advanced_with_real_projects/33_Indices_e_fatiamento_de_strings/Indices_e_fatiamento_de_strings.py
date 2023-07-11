"""
Manipulando str:

Documentação:
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html

- String índices;
- Fatiamento de strings [inicio:fim:passo];
Obs: inicia na posição informada, mas finaliza uma posição antes.
- Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

"""
# Positivos
# índice[012345678]
texto = 'Python s2'
print(texto[2])  # t
print(texto[2])  # 2
print(texto[6])  # espaço vazio

# Negativos
# índice[987654321]
texto2 = 'Python_s3'

url = 'www.google.com.br/'
print(url[:-1])  # Exibe sem o último caractére /

# Fatiando str
# Positivos
nova_string = texto2[2:6]  # não será incluido o 6.
print(nova_string)
nova_string2 = texto2[:6]  # início até a 5 posição.
print(nova_string2)
nova_string3 = texto2[7:]  # inícia na posicao 7 até o final.
print(nova_string3)

# Negativos
# 'Python s3'  [-9,-8,-7,-6,-5,-4,-3,-2,-1]
nova_string4 = texto2[-1]  # Última posição.
print(nova_string4)
nova_string5 = texto2[-9]  # Primeira posição.
print(nova_string5)
nova_string6 = texto2[-9:-1]  # Primeira posição até a penúltima.
print(nova_string6)

# Pulando caractéres [inicio:fim:passo]
nova_string7 = texto2[0:7:2]
print(nova_string7)
nova_string7 = texto2[0::3]  # Do inicio até o final de 3 em 3.
print(nova_string7)
