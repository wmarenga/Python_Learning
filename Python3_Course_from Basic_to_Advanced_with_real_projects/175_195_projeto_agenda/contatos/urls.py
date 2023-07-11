from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # !contato_id é um argumento que será enviado para => def ver_contato(request, contato_id):
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),
]
