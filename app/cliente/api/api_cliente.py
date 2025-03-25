from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from cliente.models import Cliente
from cliente.serializers.serializers_cliente import ClienteSerializers
from rest_framework.decorators import api_view
import requests
import json


@api_view(["GET"])
def api_listar_cliente(request):
    if request.method == "GET":
        cliente = Cliente.objects.all()
        serializer = ClienteSerializers(cliente, many=True)
        return Response(serializer.data)


@api_view(["POST"])
def api_cadastrar_cliente(request):
    serializer = ClienteSerializers(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def api_listar_cliente_cpf(request, cpf):
    if request.method == "GET":
        cliente = Cliente.objects.filter(cpf=cpf)
        if cliente:
            serializer = ClienteSerializers(cliente, many=True)
            return Response(serializer.data)
        else:
            return Response({"mensagem: Cliente inexistente"})


@api_view(["POST"])
def api_login(request, token):
    url = "https://hpnlyeee38.execute-api.us-east-1.amazonaws.com/login"

    payload = json.dumps({
        "user": "User Teste",
        "cpf": "917.892.584-45",
        "email": "teste@gmail.com"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        return Response(response.json())
        #return Response({"mensagem": "Olá! Confirmamos que você está cadastrado em nosso sistema. Se precisar de algo, estamos à disposição!"}, status=response.status_code)
    else:
        return Response({"mensagem": "Erro ao fazer login"}, status=response.status_code)