from django.contrib import admin
from django.urls import path
from cadastro.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("registrar-pessoa/", registrar_pessoa, name="registrar_pessoa"),
    path("registrar-votacao/", registrar_votacao, name="registrar_votacao"),
    path("registrar-opcao-voto/", registrar_opcao, name="registrar_opcao"),
    path("listar-pessoas/", listar_pessoas, name="listar_pessoas"),
]
