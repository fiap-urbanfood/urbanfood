from django.urls import path
from produtos import views
from produtos.api import api_produtos

urlpatterns = [
    path(
        "api_listar_produtos",
        api_produtos.api_listar_produtos,
        name="api_listar_produtos",
    ),
    path(
        "api_atualizar_produtos/<int:pk>/",
        api_produtos.api_atualizar_produtos,
        name="api_atualizar_produtos",
    ),
    path(
        "api_criar_produtos",
        api_produtos.api_criar_produtos,
        name="api_criar_produtos",
    ),
    path(
        "api_deletar_produtos/<int:pk>/",
        api_produtos.api_deletar_produtos,
        name="api_deletar_produtos",
    ),
    path(
        "api_produtos_categoria/<str:categoria>/",
        api_produtos.api_produtos_categoria,
        name="api_produtos_categoria",
    ),
]
