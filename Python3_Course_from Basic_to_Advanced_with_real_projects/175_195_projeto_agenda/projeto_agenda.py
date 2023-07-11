"""
Documentação Django:
https://docs.djangoproject.com/en/4.1/

### PROJETO AGENDA - DJANGO ###

Passo a passo:

1) Iniciando um projeto (agenda):
>> django-admin startproject agenda .
* Mover a pasta do projeto e o arquivo manage.py para pasta que preferir

2) Criamos um novo app (contatos):
>> python 175_195_projeto_agenda/manage.py startapp contatos
* Mover a pasta contatos para a pasta do projeto

3) Ir em agenda/settings.py e inserir (registrar paginas):
INSTALLED_APPS = [
    'contatos.apps.ContatosConfig',
]

4) Criar um urls em agenda para o app contatos:
urlpatterns = [
    path('', include('contatos.urls')),
    path('admin/', admin.site.urls),
]

5) Criar o arquivo urls.py em contatos (inserir comando abaixo):
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

6) Entrar em contatos/views.py e inserir a função (index):

def index(request):
    return render(request, 'contatos/index.html')

7) Dentro de contatos, criar o diretório templates;

8) Dentro de contatoss/templates, criar o diretório contatos;

9) Dentro de contatos/templates/contatos, criar (index.html):

10) Criar uma pasta templates na raiz do projeto;

11) Dentro de templates, criar um arquivo base.html (copiar um conteúdo HTML para o base);

12) Criar uma pasta chamada static em (templates/base.html) e mover pasta vendor com CSS e JS;

13) Abrir o arquivo templates/base.html;
* habilita para usar arquivos estáticos
{% load static %} # Inserir na primeira linha

* Alterar os links com a tag static do Django (paginas/...)
<!-- Bootstrap core CSS -->
<link href="{% static 'vendor/bootstrap/css/bootstrap.min.css'%}" rel="stylesheet">

<!-- Bootstrap core JavaScript -->
<script src="{% static 'vendor/jquery/jquery.slim.min.js'%}"></script>
<script src="{% static 'vendor/bootstrap/js/bootstrap.bundle.min.js'%}"></script>

14) Mover algumas linhas de comandos de templates/base.html:
de <h1> até </table>

15) Abrir o arquivo templates/contatos/index.html e extender para o base.html
{%extends 'base.html'%}
{%block conteudo%}
"inserir as linhas de HTML acima"
{%endblock%}

16) Criar uma referência em base.html para buscar em index.html (no exato local
das linha de comando movidas - html):
{%block conteudo%} {%endblock%}

17) Mover título para cima (logo abaixo de <head>):
<title>Agenda</title>

18) Criando arquivos parciais para diminuir repetições:
- Dentro de templates criar uma pasta chamada parciais;
- Criar os arquivos parciais dentro da pasta parciais;
- Criar _head.html e jogar conteúdo de <head> em base.html;
- Incluir um {% load static%} no início do html para carregar
os arquivos estáticos;
- Incluir em base.html a associação com o parciais/_head.html
(no exato local que foram movidas as linhas de comandos);
{% include 'parciais/_head.html'%}
! Fazer o mesmo procedimento para outros arquivos parciais
! (navigations, etc)

19) Inserir uma urls no <!-- Navigation --> de base.html:
* urls do app (contatos)
<a class="navbar-brand" href="{% url 'index'%}">Agenda</a>

20) Abrir o agenda/settings.py (agora o Django busca por templates na pasta
templates):
import os
TEMPLATES = [
        'DIRS': [os.path.join(BASE_DIR, 'templates')],

21) Em settings também mostrar para o Django onde buscar arquivos estáticos
na pasta de templates:

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'templates/static')
]

22) Iniciar o servidor para verificar se existe algum erro:
>> python 175_195_projeto_agenda/manage.py runserver

### CRIAÇÃO DOS MODELOS ###

1) A configuração da base de dados é feita em agenda/settings:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

2) Migração dos módulos já criados:
- Quando executamos o runserver, verificamos em vermelho um comando que deve ser executado
para a migração dos módulos (python 175_195_projeto_agenda/manage.py migrate).
* Sempre que criarmos novos módulos, teremos que executar a migração dos mesmos.
- Após executar a migração serão migradas para a base de dados (db.sqlite3).

3) Criação dos "models" (contatos/models.py):

4) Após criar todos os models, temos que migrá-los:
* Criação do arquivo das migrações:
>> python 175_195_projeto_agenda/manage.py makemigrations
- Será criado um arquivo 0001_initial.py em (contatos/migrations)
* Efetiva migração:
>> python 175_195_projeto_agenda/manage.py migrate

5) Após qualquer alteração, temos que executar os 2 comando novamente:
>> python 175_195_projeto_agenda/manage.py makemigrations
>> python 175_195_projeto_agenda/manage.py migrate

### CRIANDO O USUÁRIO DA ÁREA ADMINISTRATIVA DO DJANGO ###

1) Iniciar o servidor:
>> python 175_195_projeto_agenda/manage.py runserver

2) Entrar na área de admin do Django (entrar no browser):
http://127.0.0.1:8000/admin/login/?next=/admin/
* Nesta área é possível observar (username e password), porém ainda não criados

3) Criando o administrador (superuser):
>> python 175_195_projeto_agenda/manage.py createsuperuser
Username (leave blank to use 'marenga'): marenga
Email address: email@gmail.com
Password: 123456
Password (again): 123456
!This password is too short. It must contain at least 8 characters.
!This password is too common.
!This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

4) Iniciar o servidor novamente:
>> python 175_195_projeto_agenda/manage.py runserver

5) Acessar o browser (http://127.0.0.1:8000/admin/)

6) Entrar com o username e passord;
* A área administrativa já vem pronta para usar.

7) Entrar em contatos/admin.py e registrar os modelos:

# Importa as classes criadas em models.py
from .models import Categoria, Contato

# Para aparecer no site
admin.site.register(Categoria)
admin.site.register(Contato)


8) Refresh no browser e podemos visualizar a categoria (criada em models.py):
* Podemos adicionar e remover categorias pelo browser.

9) Para mudar o nome da categoria (Categoria object (1), Categoria object (2), etc)
e exibir o nome criado pelo usuário (contatos/models.py):

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

! Fazer o mesmo para todas as variáveis necessárias de cada classe.

class Contato(models.Model):
    # As variáveis terão um limite de 255 caractéres
    # blank=True para os parâmetros opcionais
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    # Para gerar automaticamente a data de criação
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    # Relaciona as duas tabelas(class Categoria e Contato).
    # Se não inserírmos (on_delete), todos os contatos serão apagados quando deletarmos a categoria.
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome

10) Criando contatos:
- No browser click em +Add e ADD CONTATO +;
- Todos os campos em negrito são de preenchimento obrigatório;
- Os campos não obrigatórios, estão com blank=True;
- Podemos adicionar categorias, se necessário;
- Salvar.

11) Poderíamos visualir mais campos do contato (além do nome somente):
- Ir em contatos/admin.py e criar uma classe:
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone',
                    'email', 'data_criacao', 'categoria')

# Para aparecer no site
admin.site.register(Contato, ContatoAdmin)

12) Adcionar link para clicar no nome e sobrenome:

class ContatoAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'nome', 'sobrenome')

13) Criando um filtro para nome e sobrenome:
class ContatoAdmin(admin.ModelAdmin):
    list_filter = ('nome', 'sobrenome')

14) Listar por quantidade de elementos por página:
class ContatoAdmin(admin.ModelAdmin):
    list_per_page = 10

15) Campo para busca:
class ContatoAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'sobrenome', 'telefone')

### Exibindo valores nas views ###

16) Ir em contatos/views e importat o models.py (class Contato);
from .models import Contato

- Adicionar (views.py):
def index(request):
    ! Obtem todos os contatos
    contatos = Contato.objects.all()
    ! cria um dicionário como parâmetro de render para cada index: valor 
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })
- Ir em contatos/templates/contatos/index.html e apagar:
    <tr>
        <td>
        <a href="#"> Leandro</a>
        </td>
        <td>Moreira</td>
        <td>35 9 8888-5555</td>
        <td>Família</td>
    </tr>
    <tr>
        <td>
        <a href="#"> Fátima</a>
        </td>
        <td>Oliveira</td>
        <td>35 9 9999-4352</td>
        <td>Conhecidos</td>
    </tr>

- Fazer um "for" em index.html do Djando em ('contatos': contatos) do views:
* Serão exibidos todos os contatos na agenda, inseridos dinamicamente.
    <tbody>
        {% for contato in contatos %}
            <tr>
                <td>
                    <a href="#">{{ contato.nome }}</a>
                </td>
                <td>{{ contato.sobrenome }}</td>
                <td>{{ contato.telefone }}</td>
                <td>{{ contato.categoria }}</td>
            </tr>
        {% endfor %}
    </tbody>

### Adicionando links nos contatos de agenda ###

17) Ir em contatos/urls.py e criaremos mais um end point:
urlpatterns = [
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),
]

18) Ir em contatos/views.py e criar outra função:

def ver_contato(request, contato_id):
    # ! Iremos visualizar apenas um contato
    contato = Contato.objects.get(id=contato_id)
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })

19) Criar um novo html em contatos/templates/contatos (ver_contato.html):
- Apagar todo o conteúdo e deixar somente as tags de abertura e fechamento de bloco (Django);
- Copiar de <h1> até o final de </dl>;
- Entrar em ver_contato.html e alterar os parâmetros;
{%block conteudo%}

<h1 class="mt-5">{{ contato.nome }}</h1>
<dl>
    <dt>ID</dt>
    <dd>{{ contato.id }}</dd>

    <dt>Telefone</dt>
    <dd>{{ contato.telefone }}</dd>

    <dt>E-mail</dt>
    <dd>{{ contato.email }}</dd>

    <dt>Data criação</dt>
    <dd>{{ contato.data_criacao }}</dd>

    <dt>Categoria</dt>
    <dd>{{ contato.categoria }}</dd>

    <dt>Descrição</dt>
    <dd>{{ contato.descricao }}</dd>
</dl>

{%endblock%}

20) Agora iremos corrigir o url, utilizando o name de urls.py em index.html
- path('<int:contato_id>', views.ver_contato, name='ver_contato'),
- <td>
    # ! Irá abrir os contatos de acordo com seu id correspondente.
    <a href="{% url 'ver_contato' contato.id %}">{{ contato.nome }}</a>
  </td>

21) Alterar para exibir o também:
- Ir em contatos/templates/contatos/ver_contato.html e inserir o contato.sobrenome
<h1 class="mt-5">{{ contato.nome }} {{ contato.sobrenome }}</h1>

22) Alterar a data de craição para formato português:
    <dt>Data criação</dt>
    <dd>{{ contato.data_criacao|date:'d/n/Y H:i:s' }}</dd>

### Levantando erros 404 ###

! Quando digitamos um ip da url com um id que não existe, o Django mosta o erro 500,
! onde o código de erro correto seria 404 (página não existe).
https://pt.wikipedia.org/wiki/Lista_de_c%C3%B3digos_de_estado_HTTP

23) Ir em contatos/views.py e importar:

from django.shortcuts import get_object_or_404

def ver_contato(request, contato_id):
    # ! Iremos visualizar apenas um contato e o método get() só retorna um valor e não iterável.
    # contato = Contato.objects.get(id=contato_id)
    # Exibe o erro 404 quando a página não existir
    contato = get_object_or_404(Contato, id=contato_id)
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })

### USANDO CONDICIONAIS ###

24) Iniciar o servidor:
>> python 175_195_projeto_agenda/manage.py runserver

25) Entrar na área administrativa e logar:

http://127.0.0.1:8000/admin/
login: marenga
senha: 123456

26) Entrar em contatos:
! Alterações propostas
- Editar o campo telefone para que possa ser alterados diretamente, sem entrar no contato;
- Criar um campo chamado "mostrar" depois de "categoria", para habilitar se ele deve ser
exibido ou não nos contatos.

27) Criação do campo "mostrar":
- Ir em contatos/models.py e criar um novo campo mostrar em class Contato (após categoria);

class Contato(models.Model):
    mostrar = models.BooleanField(default=True)

28) Após inserir, temos que fazer a migração dos novos dados:
>> python 175_195_projeto_agenda/manage.py makemigrations
* Efetiva migração:
>> python 175_195_projeto_agenda/manage.py migrate

29) Editar a área administrativa para mostrar o campo "mostrar":
- Ir em contatos/admin.py e acrescentar o campo "mostrar":

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone',
                    'email', 'data_criacao', 'categoria', "mostrar")

30) Editar sem precisar entrar no contatos:
- Entrar em contatos/admin e inserir uma linha de comando após "search_fields":

class ContatoAdmin(admin.ModelAdmin):
    list_editable = ('telefone', 'mostrar')

31) Utilizando o campo criado:
- Ir em contatos/templates/contatos/indedx.html e criar uma condição (for):
* Se contato.mostrar for verdadeiro, mostrar o contato.
    <tbody>
        {% for contato in contatos %}
            {% if contato.mostrar %}
                <tr>
                    <td>
                        <a href="{% url 'ver_contato' contato.id %}">{{ contato.nome }}</a>
                    </td>
                    <td>{{ contato.sobrenome }}</td>
                    <td>{{ contato.telefone }}</td>
                    <td>{{ contato.categoria }}</td>
                </tr>
            {% endif %}
        {% endfor %}
    </tbody>

### PAGINAÇÃO ###

32) Primeiro importar "Paginator":

- Ir em contatos/views.py e importar o "Paginator".

from django.core.paginator import Paginator

def index(request):
    contatos = Contato.objects.all()
    paginator = Paginator(contatos, 10)  # Show 10 contacts per page.

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

33) Usar paginação de um Bootstrap (Google: pagination bootstrap):

- Ir em contatos/templates/contatos/index.html e colar no final do html
(antes do final do bloco):

</table>

<nav aria-label="Page navigation example">
    <ul class="pagination">
        {% for pagina in contatos.paginator.page_range %}
            <li class="page-item">
                <a class="page-link" href="?p={{ pagina }}">{{pagina}}</a>
            </li>
        {% endfor %}
    </ul>
</nav>

{%endblock%}

34) Adicionar uma sinalização para destacar a página que está ativa:

<nav aria-label="Page navigation example">
    <ul class="pagination">
        {% for pagina in contatos.paginator.page_range %}
            {% if contatos.number == pagina %}
                <li class="page-item active">
                    <a class="page-link" href="?p={{ pagina }}">{{pagina}}</a>
                </li>
            {% else %}
                <li class="page-item">
                    <a class="page-link" href="?p={{ pagina }}">{{pagina}}</a>
                </li>
            {% endif %}
        {% endfor %}
    </ul>
</nav>

35) Correção de problema (exibição de contato oculto):
! Quando o ID do contato é digitado na url, o nome ainda aparece.

- Ir em contatos/views.py;

"""
