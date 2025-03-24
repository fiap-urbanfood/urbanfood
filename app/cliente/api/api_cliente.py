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
def api_login(request):
    url = "https://hpnlyeee38.execute-api.us-east-1.amazonaws.com/login"

    payload = json.dumps({
        "user": "User Teste",
        "cpf": "060.531.410-11",
        "email": "teste@gmail.com"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJraWQiOiJ5WlBRc08wRmowXC9kM21JS0d5cHhvZzFlRzZ4XC85T2tLMjZTbFwvMnBoMEtJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxb2ZsM2c5dTA0ZWY5Mzg2MWN0MzMyNnBpZCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiZGVmYXVsdC1tMm0tcmVzb3VyY2Utc2VydmVyLXI1eWVncVwvcmVhZCIsImF1dGhfdGltZSI6MTc0MjI1MTI0NywiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfSUk3Z0NvUHJJIiwiZXhwIjoxNzQyMjU0ODQ3LCJpYXQiOjE3NDIyNTEyNDcsInZlcnNpb24iOjIsImp0aSI6ImZjN2Q2ZTY3LWNjYjYtNGU5Ni05NDc5LWM1YjZiMDRmNGY0NiIsImNsaWVudF9pZCI6IjFvZmwzZzl1MDRlZjkzODYxY3QzMzI2cGlkIn0.sbDHS0NeDv9QVIuTufxhF3soZDB5p-R5CEZTBstQ9qROIjozYgxYizk-SoNl3VHz_If8DQLklLlnN_wp13bsNOJh5t9zUO7SQvj0PWlHqonwY0hdFP8-KqdLy0CcIVQeDT-bDSN5tJe7XXjDTOyhE5-fzs1UtitjBb63Qa7J7_gqYsC3BD5Qn4ZZo1-dJ0B_FoUgb_0XK7bpDCgjMYu__6RI1d8RNjN3TVs-9pd-rd9v8Keat_Z6Di9zTLU6GfcdudiqHaHRuJusLQAI62Yk-8kBlEjh0xf3AM1KYg77ai8i0tgSNs7XKJuvAUTKAgdOHarYUX-FFj1FsBV0PCY46g'
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        #return Response(response.json())
        return Response({"mensagem": "Usuario Localizado com cpf --"}, status=response.status_code)
    else:
        return Response({"mensagem": "Erro ao fazer login"}, status=response.status_code)