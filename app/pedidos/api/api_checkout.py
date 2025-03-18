from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from pedidos.models import Pedidos, Checkout
from pedidos.serializers.serializers_checkout import CheckoutSerializers
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
import mercadopago
from produtos.models import Produtos
from django.shortcuts import render


@api_view(["POST"])
def api_cadastrar_checkout(request):
    serializer = CheckoutSerializers(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def api_listar_checkout(request):
    if request.method == "GET":
        checkout = Checkout.objects.all()
        serializer = CheckoutSerializers(checkout, many=True)
        return Response(serializer.data)


@api_view(["PUT"])
def api_checkout(request, pk):
    checkout = get_object_or_404(Checkout, pk=pk)
    serializer = CheckoutSerializers(checkout, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def api_checkout2(request, produtoId, checkoutId):
    try:
        produtos = get_object_or_404(Produtos, pk=produtoId)
        print(type(produtos.preco_unitario))
        print(checkoutId)
        sdk = mercadopago.SDK("TEST-2489955470919494-121607-9c3ad5468a7beffe4259f75cf7aa4d92-431795054")
        payment_data = {
            "items": [
                {"id": produtos.pk, "title": produtos.nome, "quantity": 1, "currency_id": "BRL",
                 "unit_price": produtos.preco_unitario}
            ],
            "back_urls": {
                f"success": f"http://127.0.0.1:8000/pedidos/compracerta/{checkoutId}",
                "failure": "http://127.0.0.1:8000/pedidos/compraerrada",
                "pending": "http://127.0.0.1:8000/pedidos/compraerrada",
            },
            "auto_return": "all"
        }
        result = sdk.preference().create(payment_data)
        payment = result["response"]
        link_iniciar_pagamento = payment["init_point"]
        # print(payment)
        return Response({"Acesse o link para efetuar o pagamento:" + link_iniciar_pagamento})
    except:
        print("produtos.pk")
        return Response({"mensagem:" + "Produto não encontrado"})


@api_view(["GET"])
def compracerta(request, pk):
    checkout = get_object_or_404(Checkout, pk=pk)
    checkout.status = True
    checkout.save()
    return render(request, "pedidos/index.html")
    # return Response({"mensagem:" + "Compra concluida com sucesso"})


@api_view(["GET"])
def cartoes_teste(request):
    return render(request, "pedidos/cartoes_teste_brasil.html")
