from django.urls import path
from cliente import views
from cliente.api import api_cliente

urlpatterns = [
    path("", views.cliente, name="cliente"),
    path(
        "api_listar_cliente", api_cliente.api_listar_cliente, name="api_listar_cliente"
    ),
    path(
        "api_cadastrar_cliente",
        api_cliente.api_cadastrar_cliente,
        name="api_cadastrar_cliente",
    ),
    path(
        "api_listar_cliente_cpf/<str:cpf>/",
        api_cliente.api_listar_cliente_cpf,
        name="api_listar_cliente_cpf",
    ),

       path(
        "login_cpf_api_lambda",
        api_cliente.api_login,
        name="api_listar_cliente_cpf",
    ),
]
