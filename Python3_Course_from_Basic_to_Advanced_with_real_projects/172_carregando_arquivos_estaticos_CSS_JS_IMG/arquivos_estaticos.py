"""
1) Iniciando um projeto (TESTE):
>> django-admin startproject TESTE .

2) Criamos um novo app (home):
>> python 172_carregando_arquivos_estaticos_CSS_JS_IMG/manage.py startapp paginas
* Mover a pasta home para a pasta do projeto

3) Ir em TESTE/settings.py e inserir (registrar paginas):
INSTALLED_APPS = [
    'paginas.apps.PaginasConfig',
]

4) Criar um urls em TESTE para o app paginas:
urlpatterns = [
    path('', include('paginas.urls')),
]

5) Criar o arquivo urls.py em paginas (inserir comando abaixo):
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
]

6) Entrar em paginas/views.py e inserir as duas funções (index e sobre):
def index(request):
    return render(request, 'paginas/index.html')

def sobre(request):
    return render(request, 'paginas/sobre.html')

7) Dentro de paginas, criar o diretório templates;

8) Dentro de paginas/templates, criar o diretório paginas;

9) Dentro de paginas/templates/paginas, criar (index.html, sobre.html):

10) Criar uma pasta templates na raiz do projeto;

11) Dentro de templates, criar um arquivo base.html (copiar um conteúdo HTML para o base);

12) Ir em TESTE/settings e informar para o Django que o templates será a 
base do projeto:
TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    },
]

13) Abrir o arquivo templates/paginas/index.html e extender para o base.html
{%extends 'base.html'%}

{%block conteudo%} INDEX {%endblock%}

14) Fazer o mesmo com o templates/paginas/sobre.html e extender para o base.html
{%extends 'base.html'%}

{%block conteudo%} SOBRE {%endblock%}

15) Carregar o servidor:
>> python 172_carregando_arquivos_estaticos_CSS_JS_IMG/manage.py runserver

### COMEÇANDO A CRIAR OS ARQUIVOS ESTÁTICOS ###

1) Criar uma pasta chamada (paginas/static);

2) Dentro de static, criar uma nova pasta chamada paginas;

3) Copiar a pasta vendor para static/paginas;

4) Abrir o arquivo templates/base.html;
** habilita para usar arquivos estáticos
{% load static %} # Inserir na primeira linha

** Alterar os links com a tag static do Django (paginas/...)
<!-- Bootstrap core CSS -->
<link href="{% static 'paginas/vendor/bootstrap/css/bootstrap.min.css'%}" rel="stylesheet">

<!-- Bootstrap core JavaScript -->
<script src="{% static 'paginas/vendor/jquery/jquery.slim.min.js'%}"></script>
<script src="{% static 'paginas/vendor/bootstrap/js/bootstrap.bundle.min.js'%}"></script>

### CONFIGURANDO OS LINKS ###

1) Abrir o arquivo templates/base.html;

2) Apagar os links (deixar: home e sobre):

<li class="nav-item">
<a class="nav-link" href="#">Serviços</a>
</li>
<li class="nav-item">
<a class="nav-link" href="#">Contato</a>
</li>

3) O home vai apontar para / e sobre para /sobre:

<a class="nav-link" href="/">Home

<a class="nav-link" href="/sobre">Sobre</a>

4) Mover a pasta static para a pasta templates/base.html;

5) Mover pasta vendor para ficar direto abaixo de static (1 nível acima);

6) Apagar pasta paginas dentro de template/static/paginas;

7) Retirar referência statica de paginas de base.html:

<!-- Bootstrap core CSS -->
<link href="{% static 'vendor/bootstrap/css/bootstrap.min.css'%}" rel="stylesheet">

<!-- Bootstrap core JavaScript -->
<script src="{% static 'vendor/jquery/jquery.slim.min.js'%}"></script>
<script src="{% static 'vendor/bootstrap/js/bootstrap.bundle.min.js'%}"></script>

8) Precisamos mostrar para o Django onde buscar os arquivos estáticos:
- Ir em TESTE/settings.py e inserir (abaixo de: STATIC_URL = 'static/'):
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'templates/static')
]

9) Ir em templates/paginas/sobre.html e alterar o conteúdo:

{%extends 'base.html'%}
{% load static %}

{%block conteudo%}
<p>SOBRE</p>
<p>
    <img src="{% static 'img/a.jpg' %}" style="width: 640px; height: auto">
</p>
{%endblock%}

10) Criar uma pasta img em templates static e mover a imagem para dentro dela;

### Carregando URLs dinamicamente ###

1) Abrir o arquivo templates/base.html e alterar o index e o sobre:
<a class="nav-link" href="{% url 'index' %}">Home
<a class="nav-link" href="{% url 'sobre' %}">Sobre</a>

* Em paginas/urls.py, os nomes têm que ser iguais: name='index', name='sobre'

### Incluindo arquivos parciais ###

* Significa modularizar o projeto afim de evitar repetições de blocos de códigos HTML

1) Criar uma pasta "parciais" em templates/base.html (da raiz do projeto);

2) Criar um arquivo "_head.html" (o underline significa que o arquivo é parcial - opcional):
- adicional os comando HTML de <head>
* Atenção: Não esquecer de incluir a tag para carregar arquivos estáticos
{% load static %}

<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<meta name="description" content="">
<meta name="author" content="">

<title>Template Bootstrap</title>

<!-- Bootstrap core CSS -->
<link href="{% static 'vendor/bootstrap/css/bootstrap.min.css'%}" rel="stylesheet">

- Apagar as linhas de comando de base.html e inserir a tag do Django:
{% include 'parcial/_head.html' %}

3) Criar um arquivo templates/parcial/_navi.html
- Mover o bloco de comandos de <!-- Navigation --> para _navi.html
- Inserir uma tag Djando para referenciar onde estão os comando de navi na mesma posição em base.html.
{% include 'parcial/_navi.html' %}

"""
