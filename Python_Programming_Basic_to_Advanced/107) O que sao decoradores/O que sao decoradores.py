"""
Decoradores (Decorators):

O que sao decoradores?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar/ Açucar
Sintático).

   |------------------------------------|
   |          Function Decorator        |
   |------------------------------------|

|------------------------------------------|
|  |------------------------------------|  |
|  |          Function decorada         |  |
|  |------------------------------------|  |
|------------------------------------------|

# Decorators como funções (Sintaxe não recomendada, Sem Açucar Sintático)
# Seria o mesmo que funções aninhadas!!!


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        # O que for inserido em funcao() irá aparecer aqui ('Seja bem-vindo(a)
        # à Geek University').
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem-vindo(a) à Geek University')


# Testando 1
teste = seja_educado(saudacao)
teste()

# Testando 2


def raiva():
    print('EU TE ODEIO!')


raiva_educada = seja_educado(raiva)

raiva_educada()

# Decorators com Syntax Sugar (Açucar Sintático)


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')


# Testando
apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir')


dormir()

|-----------------------------------------------------|
|  Home  |  Serviços  |  Produtos  |  Administrativo  |
|-----------------------------------------------------|

http://www.suaempresa.com.br/home

http://www.suaempresa.com.br/servicos

http://www.suaempresa.com.br/produtos

http://www.suaempresa.com.br/admin


Obs: Não é código funcional (que funcione), é apenas exemplo

def checa_login():
    if not request.usuario:
        redirect('http://www.suaempresa.com.br/register')


def home(request):
    return 'Pode acessar home'


@checa_login
def servicos(request):
    return 'Pode acessar serviços'


def produtos(request):
    return 'Pode acessar produtos'


@checa_login
def admin(request):
    return 'Pode acessar admin'

Obs: Não confunda Decorator com Decorator Function

Decoration Function

def checa_login():
    if not request.usuario:
        redirect('http://www.suaempresa.com.br/register')

Decorator

@checa_login
"""
