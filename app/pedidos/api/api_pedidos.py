from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from pedidos.models import Pedidos
from pedidos.serializers.serializers_pedidos import PedidosSerializers, PedidosStatusSerializers
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


@api_view(["GET"])
def api_listar_pedidos(request):
    if request.method == "GET":
        pedidos = Pedidos.objects.all()
        serializer = PedidosSerializers(pedidos, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def api_listar_pedidos_status(request, status):
    if request.method == "GET":
        pedidos = Pedidos.objects.filter(status=status)
        serializer = PedidosSerializers(pedidos, many=True)
        return Response(serializer.data)

@api_view(["POST"])
def api_cadastrar_pedidos(request):
    serializer = PedidosSerializers(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["PUT"])
def api_atualizar_status_pedidos(request, pk):
    pedidos = get_object_or_404(Pedidos, pk=pk)
    serializer = PedidosStatusSerializers(pedidos, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def api_deletar_pedidos(request, pk):
    pedidos = get_object_or_404(Pedidos, pk=pk)
    pedidos.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)