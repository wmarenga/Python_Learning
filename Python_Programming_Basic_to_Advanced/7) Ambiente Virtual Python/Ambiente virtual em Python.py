'''
Instalacao de duas bibliotecas de Ambiente Virtual
- virtualenv
- virtualenvwrapper

pip install virtualenv virtualenvwrapper-win
  
- Adicionar uma pasta (Envs) em local determinando (em variaveis de ambiente do Windows)
Ex.: D:\23) Programação\Cursos\Python\Envs
- Verificar se a variavel esta sendo reconhecida com o nome atribuido a variavel de ambiente (Ambiente_Virtual_Python)
cmd: echo %Ambiente_Virtual_Python%
cmd: Retorna o Path da variavel

# Criacao do ambiente virtual:

cmd: mkvirtualenv env

# Processo mais simples:

- Com o Python instalado;
- Abrir o VSCode/ terminal
- digitar o comando na pasta que quer instalar o ambiente virtual
python -m venv env

# Ativacao do Ambiente Virtual

- Entrar na pasta do ambiente virtual;
- Digitar o comando (PowerShell do Windows - entrar como administrador): 
    set-ExecutionPolicy -scope CurrentUser -ExecutionPolicy RemoteSigned
- Digitar o comando: .\env\Scripts\Activate.ps1 (PowerShell)
- No CMD sera .\env\Scripts\activate.bat

# Para desativar

- Digitar o comando: deactivate (PowerShell)

# Criando um ambiente virtual para uma versao especifica do Python

mkvirtualenv projectxxx -p python3.7

python -m pip install novas

# Todos os pacotes intalados no ambiente virtual
pip list

# Removendo ambientes virtuais

rmvirtualenv projetoxxx

''' 