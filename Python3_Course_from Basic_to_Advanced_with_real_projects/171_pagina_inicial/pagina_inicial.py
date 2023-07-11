"""
Antes de carregar a página HTML, temos que rodar o servidor:
>> python 171_pagina_inicial/manage.py runserver


Para evitar a página de erro no IP do projeto:
- Criar um views.py na pasta meusite;
- Dentro do views.py inserímos os comandos
    from django.shortcuts import render

    def index(request):
        return render(request, 'home/index.html')
- Dentro de paginas/home/index.html inserimos um <h1>
- Agora precisamos apontar uma urls para a home (temos que ter uma views para isto);
- Para importar do views o urls.py do projeto (meusite), usamos:
    from . import views
    
    urlpatterns = [
        path('', views.index),
        path('admin/', admin.site.urls),
        path('blog/', include('blog.urls')),
        path('sobre/', include('sobre.urls')),

]
- Agora para usarmos o Template, abrimos paginas/home/index.html e acrescentamos os comando abaixo:
{%extends 'base.html'%}
- Para exibir texto usamos os comandos abaixo:
{%block 'titulo'%}HOME{%endblock%}

{%block 'conteudo'%}
Eu sou a home!
{%endblock%}

*** Para fazer o mesmo procedimento (criação de views em meusite), só que criando um app:
1) Criamos um novo app (home):
>> python 171_pagina_inicial/manage.py startapp home
* Mover a pasta home para a pasta do projeto

2) Ir em settings.py(meusite) e inserir o caminho do app em INSTALLED_APPS = :
'home.apps.HomeConfig',

3) Ir em urls.py, importar o views e inserir o caminho da url:
from home import views

urlpatterns = [
    path('', views.index),
]

4) Ir no views da pasta home e criar a função index:
def index(request):
    return render(request, ):

5) Criamos uma pasta templates dentro da pasta home e movemos a pasta home já
criadas dentro de páginas:

6) Ir no home/views e inserir uma função:
    def index(request):
        return render(request, 'home/index.html')
"""
