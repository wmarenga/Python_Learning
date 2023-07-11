"""
1) Instalar Django:
pip install django

2) Iniciando um projeto Django:
>> django-admin startproject meusite .

3) Criando um app (iniciando uma seção do site) - cria fora da pasta do projeto:
>> python 170_usando_um_template_HTML_em_comum/manage.py startapp blog
* Mover a pasta para a pasta do projeto
* Mover também o arquivo manage.py para a pasta do projeto

4) Ir em settings.py(meusite) e inserir o caminho do app em INSTALLED_APPS = :
'blog.apps.BlogConfig',

5) Ir em urls.py e inserir o caminho da url:
*** blog.urls é o módulo (função) que iremos importar.
*** Não esquecer de inserir o include (from django.urls import path, include)
urlpatterns = [
    path('blog/', include('blog.urls')),
]

6) Criar arquivo urls.py na pasta blog e inserir os comando abaixo:
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
]

7) Abrir o arquivo views.py em blog e definir a função index (def):
def index(request):
    return render(request, 'blog/index.html')

8) Criar pasta templates na pasta blog e dentro de template criar a pasta blog, e
dentro da pasta blog, criaremos o arquivo index.html
*** Atenção templates tem que ser com "s", senão não funcionará.

9) Antes de carregar a página HTML, temos que rodar o servidor:
>> python 170_usando_um_template_HTML_em_comum/manage.py runserver

10) No navegador digitar http://127.0.0.1:8000/blog/

11) Definindo para o Django onde procurar arquivos de templates:
- Ir em /meusite/settings.py
- Inserir: TEMPLATES = 'DIRS': [os.path.join(BASE_DIR, 'paginas')],

12) Criar arquivo base.html na pasta "/paginas"

13) Dentro do arquivo /paginas/base.html
- Mudar <title> usando a linguagem usada em Django:
*** Não esquecer de fechar o bloco com {%endblock%}

<head>
    <title>{%block 'titulo'%}{%endblock%}</title>
</head>

- Deixar um espaço para digitar coisas:

<body>
{%block 'conteudo'%}{%endblock%}
</body>

14) Dentro do arquivo /blog/templates/blog/index.html, inserir:

** Puxa do arquivo base.html
{%extends 'base.html'%}

** Chamando o bloco título em <head>
{%block 'titulo'%}Eu vou colocar o titulo.{% endblock %}

** Chamando o bloco conteúdo <body>
{%block 'conteudo'%}
<h1>Eu sou o blog.</h1>
{%endblock%}

15) Criação de uma tag <style> para visualizar melhor

    <style>
        body {
            font-size: 40;
            background: red;
            color: white;
        }
    </style>

Dica: Para ver o código fonte no navegador (windows) usamos o atalho crtl + u

*Explicação: O arquivo base.html é o código fonte, e o arquivo index.html 
*adiciona conteúdo no arquivo base.html

16) Criação de outro app (sobre):
>> python 170_usando_um_template_HTML_em_comum/manage.py startapp sobre
* Mover a pasta para a pasta do projeto

17) Ir em settings.py(meusite) e inserir o caminho do app em INSTALLED_APPS = :
'sobre.apps.SobreConfig',

18) Ir em urls.py e inserir o caminho da url:
urlpatterns = [
    path('sobre/', include('sobre.urls')),
]

19) Criar arquivo urls.py na pasta sobre e inserir os comando abaixo:
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
]

20) Abrir o arquivo views.py em /sobre e definir a função index (def):
def index(request):
    return render(request, 'sobre/index.html')

21) Dentro do arquivo /sobre/templates/sobre/index.html, inserir:
*Atenção: Não esquecer de usar o "extends" para puxar o conteúdo do arquivo base.html

** Puxa do arquivo base.html
{%extends 'base.html'%}

** Chamando o bloco conteúdo <body>

{%block 'titulo'%}Sobre - Título{%endblock%}

{%block 'conteudo'%}
<dl>
    <dt>Definition list</dt>
    <dd>Consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
 aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
 commodo consequat.</dd>
    <dt>Lorem ipsum dolor sit amet</dt>
    <dd>Consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
 aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
 commodo consequat.</dd>
 </dl>
{%endblock%}

22) Antes de carregar a página HTML, temos que rodar o servidor:
>> python 170_usando_um_template_HTML_em_comum/manage.py runserver
"""
