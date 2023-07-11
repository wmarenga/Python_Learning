from django.urls import path
from . import views

urlpatterns = [
    path('teste/', views.teste)
]
# 127.0.0.1:8000/sobre/teste
