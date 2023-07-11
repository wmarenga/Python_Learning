"""
### Referência para criação dos campos (base_dados.txt) ###

CONTATOS
nome: STR * (obrigatório)
sobrenome: STR (opcional)
telefone: STR * (obrigatório)
email: STR (opcional)
data_criacao: DATETIME (automático)
descricao: texto
categoria: CATEGORIA (outro model)

CATEGORIA
nome: STR * (obrigatório)
"""
from django.db import models
from django.utils import timezone

# A classe tem que herdar de models(trazer tudo de models para classe Contatos).


# Poderíamos criar outro model só para categoria e importálo, porém, para simplificar
# criaremos uma classe Categoria.
class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


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
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
