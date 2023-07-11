'''
Lendo e escrevendo arquivos (extra):

Estrutura para ler:

with open(caminho_string) as f:

variavel = **f.read()**

**f.close**

Exemplo:

caminho = 'D:\\23) Programação\\Cursos\Python\\Criando ambiente virtual (Visual Studio Code).txt'

#Escrevendo a estrutura para ler o arquivo
with open(caminho) as f:
    texto_1 = f.read()
    f.close()
print(texto_1)

Estrutura para escrever:

with open(nome_novo_arquivo,'w') as f:

f.write('nova_string')

**f.close**

caminho2 = 'D:\\23) Programação\\Cursos\Python\\Criando ambiente virtual (Visual Studio Code)2.txt'

#Escrevendo a estrutura para ler o arquivo
with open(caminho) as f:
    texto_2 = texto_1 + '\nF\nG\nH'
    
    # O argumento 'w' e para escrever e definimos um novo nome para o arquivo_novo
    # open(nomo_arquivo, 'w' para escrever) se o arquivo ja existir o arquivo, nao e necessario o 'w'
with open(caminho2,'w') as f:
    f.write(texto_2)
    f.close
'''