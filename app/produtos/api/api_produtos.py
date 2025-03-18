from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from produtos.models import Produtos
from produtos.serializers.serializers_produtos import ProdutosSerializers
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


@api_view(["GET"])
def api_listar_produtos(request):
    if request.method == "GET":
        produtos = Produtos.objects.all()
        serializer = ProdutosSerializers(produtos, many=True)
        return Response(serializer.data)


@api_view(["PUT"])
def api_atualizar_produtos(request, pk):
    produtos = get_object_or_404(Produtos, pk=pk)
    serializer = ProdutosSerializers(produtos, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def api_criar_produtos(request):
    serializer = ProdutosSerializers(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["DELETE"])
def api_deletar_produtos(request, pk):
    produtos = get_object_or_404(Produtos, pk=pk)
    produtos.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def api_produtos_categoria(request, categoria):
    if request.method == "GET":
        produtos = Produtos.objects.filter(categoria=categoria)
        serializer = ProdutosSerializers(produtos, many=True)
        return Response(serializer.data)