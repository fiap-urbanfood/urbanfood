from django.urls import path
from pedidos import views
from pedidos.api import api_pedidos, api_checkout

urlpatterns = [
    path(
        "api_listar_pedidos", api_pedidos.api_listar_pedidos, name="api_listar_pedidos"
    ),

    path(
        "api_listar_pedidos_status/<str:status>/", api_pedidos.api_listar_pedidos_status,
        name="api_listar_pedidos_status"
    ),

    path(
        "encaminhar_pedido_fila",
        api_pedidos.api_cadastrar_pedidos,
        name="api_cadastrar_pedidos",
    ),
    path(
        "api_atualizar_status_pedidos/<int:pk>/",
        api_pedidos.api_atualizar_status_pedidos,
        name="api_atualizar_status_pedidos",
    ),
    path(
        "ckeckout/<int:pk>/",
        api_checkout.api_checkout,
        name="ckeckout",
    ),

    path(
        "api_listar_checkout", api_checkout.api_listar_checkout, name="api_listar_checkout"
    ),
    path(
        "fake_checkout",
        api_checkout.api_cadastrar_checkout,
        name="api_cadastrar_checkout",
    ),

    path(
        "api_deletar_pedidos/<int:pk>/",
        api_pedidos.api_deletar_pedidos,
        name="api_deletar_pedidos",
    ),

    path(
        "api_checkout2/<int:produtoId>/<int:checkoutId>/", api_checkout.api_checkout2, name="api_checkout2"
    ),

    path(
        "compracerta/<int:pk>/", api_checkout.compracerta, name="compracerta"
    ),
    path(
        "cartoes_teste/", api_checkout.cartoes_teste, name="cartoes_teste"
    ),

]
