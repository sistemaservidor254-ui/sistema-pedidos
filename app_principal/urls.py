# app_principal/urls.py
from django.urls import path
from . import views_clientes
from .views_autocomplete import autocomplete_endereco

urlpatterns = [
    path("enderecos/autocomplete", autocomplete_endereco, name="autocomplete_endereco"),
    path("clientes/", views_clientes.lista_clientes, name="lista_clientes"),
    path("clientes/novo/", views_clientes.form_cliente, name="form_cliente"),
    path(
        "clientes/excluir/<int:pk>/",
        views_clientes.excluir_cliente,
        name="excluir_cliente",
    ),
]
