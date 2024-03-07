from django.contrib import admin
# Importa o objeto de banco de dados
from .models import PessoaBancoDeDados

# Register your models here.

admin.site.register(PessoaBancoDeDados)